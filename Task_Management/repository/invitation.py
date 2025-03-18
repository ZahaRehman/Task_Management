from sqlalchemy.orm import Session
import secrets
from fastapi import HTTPException, status
from .. import models, Schemas

def create_invitation(project_id: int, invitation: Schemas.InvitationCreate, db: Session, current_user: Schemas.User):
    if current_user.role not in ["admin", "manager"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to invite users"
        )

    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )

    token = secrets.token_hex(16)
    new_invitation = models.Invitation(
        project_id=project_id,
        invited_email=invitation.invited_email,
        token=token,
        status="pending"
    )
    db.add(new_invitation)
    db.commit()
    db.refresh(new_invitation)
    return new_invitation

def accept_invitation(invitation_accept: Schemas.InvitationAccept, db: Session, current_user: Schemas.User):
    
    invitation = db.query(models.Invitation).filter(models.Invitation.token == invitation_accept.token).first()
    if not invitation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invitation not found"
        )

    if invitation.status != "pending":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invitation already accepted or invalid"
        )

    if current_user.email != invitation.invited_email:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This invitation is not for your email"
        )

    invitation.status = "accepted"
    db.commit()
    db.refresh(invitation)


    return invitation

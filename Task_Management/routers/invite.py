from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import Schemas, models, database, oauth2
from ..repository import invitation

router = APIRouter(
    tags=["Invitation"]
)

@router.post("/projects/{project_id}/invite", response_model=Schemas.InvitationResponse)
def invite_user(
    project_id: int,
    invitation_data: Schemas.InvitationCreate,
    db: Session = Depends(database.get_db),
    current_user: Schemas.User = Depends(oauth2.get_current_user)
):
    return invitation.create_invitation(project_id, invitation_data, db, current_user)


@router.post("/invitations/accept", response_model=Schemas.InvitationResponse)
def accept_invitation(
    invitation_accept: Schemas.InvitationAccept,
    db: Session = Depends(database.get_db),
    current_user: Schemas.User = Depends(oauth2.get_current_user)
):
    return invitation.accept_invitation(invitation_accept, db, current_user)

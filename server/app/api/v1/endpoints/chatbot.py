from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from app.api import deps
from app.services.chatbot import chatbot_service

router = APIRouter()

class ChatMessage(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@router.post("/chat", response_model=ChatResponse)
def chat(
    *,
    message: ChatMessage,
    current_user = Depends(deps.get_current_active_user),
):
    """
    Chat with the AI assistant.
    """
    try:
        response = chatbot_service.get_response(message.message)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing chat message: {str(e)}"
        ) 
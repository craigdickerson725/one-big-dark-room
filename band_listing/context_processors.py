from .models import Message

# Context processor to count unread messages for the logged-in user
def unread_message_count(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Count unread messages for the authenticated user
        unread_count = Message.objects.filter(recipient=request.user, is_read=False).count()
    else:
        # If user is not authenticated, set unread message count to 0
        unread_count = 0
    
    # Return the unread message count as a context dictionary
    return {'unread_count': unread_count}

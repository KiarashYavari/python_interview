import base64
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from googleapiclient.discovery import build
from authentication import authenticate


creds = authenticate()  # Reuse the authentication function
service = build('gmail', 'v1', credentials=creds)
gmail_api_obj = service.users().messages()

def get_unread_gmails(next_page_token=None):
    
    # Use the Gmail query to find unread emails
    query = 'is:unread'
    
    try:
        # Search for unread emails
        results = gmail_api_obj.list(userId='me', q=query,\
                                                  pageToken=next_page_token)\
                                                      .execute()
        messages = results.get('messages', [])
        next_page_token = results.get('nextPageToken')
        
        if not messages:
            print("No unread emails found.")
        else:
            print(f"Found {len(messages)} unread emails:")
            for message in messages:
                # Fetch the email details using the message ID
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                headers = msg['payload']['headers']
                
                # Extract the 'From' and 'Subject' fields from the email headers
                from_header = next(header['value'] for header in headers if header['name'] == 'From')
                subject_header = next(header['value'] for header in headers if header['name'] == 'Subject')
                
                print(f"From: {from_header}, Subject: {subject_header}")
    
    except Exception as error:
        print(f'An error occurred: {error}')
    
    return next_page_token
        
# get unread gmails func call
page_token = get_unread_gmails()

while page_token:
    print("\nFetching the next page of emails...\n")
    page_token = get_unread_gmails(next_page_token=page_token)


def send_email_with_attachment(service, user_id, recipient, subject, message_text, attachment_file):
    """
    Sends an email with an attachment via Gmail API.

    Parameters:
    - service: Authorized Gmail API service instance.
    - user_id: The user's email address ('me' for the authenticated user).
    - recipient: Email address of the recipient.
    - subject: Subject of the email.
    - message_text: The body of the email.
    - attachment_file: Path to the file to be attached.

    Returns:
    - Sent email's message object.
    """

    # Create a MIME multipart message
    message = MIMEMultipart()
    message['to'] = recipient
    message['from'] = user_id
    message['subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(message_text, 'plain'))

    # Attach the file
    if attachment_file:
        # Read the file and attach it
        content_type, encoding = None, None
        file_name = os.path.basename(attachment_file)
        with open(attachment_file, 'rb') as f:
            file_data = f.read()

        # Create the MIMEBase object
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file_data)

        # Encode the payload using Base64 and add necessary headers
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename="{file_name}"',
        )

        # Attach the part to the message
        message.attach(part)

    # Encode the message as base64
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    # Create the message payload to send
    body = {'raw': raw_message}

    try:
        # Send the email
        message = gmail_api_obj.send(userId=user_id, body=body).execute()
        print(f"Message sent with ID: {message['id']}")
        return message
    except Exception as error:
        print(f"An error occurred: {error}")
        return None

# Usage
# send_email_with_attachment(
#     service=service,
#     user_id='me',
#     recipient='kiarash996@yahoo.com',
#     subject='Test Email with Attachment',
#     message_text='Please find the attached document. this is a test email sent with google client API',
#     attachment_file='ghodrate-kalam.pdf'
# )

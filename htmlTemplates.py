<<<<<<< HEAD
css = '''
<style>
/* Global styling for the entire screen */
body {
    background-color: #303030; /* Dark grey background */
    color: white !important; /* White text color */
    font-family: 'Arial', sans-serif; /* Font family */
}

/* Input field styling */
input[type="text"] {
    background-color: white !important; /* White background for input */
    outline: none !important; /* Remove the default outline */
    box-shadow: none !important; /* Remove any default shadow */
}

/* Label text for input boxes */
label {
    color: white !important; /* White label text */
}

/* Main content area styling */
.stApp {
    background-color: #303030; /* Dark grey background */
    color: white !important; 
}

/* Header styling */
h1, h2, h3, h4, h5, h6 {
    color: white !important; /* White color for headers */
    text-align: center; /* Centered text */
    font-weight: bold; /* Bold headers */
    margin-bottom: 1rem; /* Space below headers */
}

/* Header background */
header {
    background-color: #303030 !important; /* Dark grey background */
}

/* Global styling for the entire screen */
body {
    background-color: #303030; /* Dark grey background */
    color: white; /* White text color */
    font-family: 'Arial', sans-serif; /* Font family */
}

/* Chat container styling */
.chat-container {
    max-height: 400px; /* Fixed height */
    width: 100%; /* Full width */
    overflow-y: auto; /* Vertical scrolling enabled */
    padding: 10px; /* Padding inside the container */
    background-color: #2B2B2B; /* Dark background */
    border-radius: 10px; /* Rounded corners */
    border: 1px solid #fff; /* White border */
    margin-top: 20px; /* Space above container */
}

/* Chat message styling */
.chat-message {
    display: flex; /* Use flexbox for avatar and message alignment */
    margin-bottom: 10px; /* Space between messages */
    word-wrap: break-word; /* Break long words */
}

/* User message styling */
.chat-message.user .message {
    background-color: #2b313e; /* Dark background for user */
    padding: 10px; /* Padding inside message */
    border-radius: 8px; /* Rounded edges */
    color: #fff; /* White text */
    margin-left: 10px; /* Add space from avatar */
}

/* Bot message styling */
.chat-message.bot .message {
    background-color: #475063; /* Dark background for bot */
    padding: 10px; /* Padding inside message */
    border-radius: 8px; /* Rounded edges */
    color: #fff; /* White text */
    margin-left: 10px; /* Add space from avatar */
}

/* Avatar styling */
.chat-message .avatar img {
    width: 35px; /* Avatar width */
    height: 35px; /* Avatar height */
    border-radius: 50%; /* Circular avatars */
}

/* Scrollbar styling */
.chat-container::-webkit-scrollbar {
    width: 8px; /* Scrollbar width */
}

.chat-container::-webkit-scrollbar-thumb {
    background-color: #666; /* Scrollbar thumb color */
    border-radius: 4px; /* Rounded scrollbar thumb */
}

.chat-container::-webkit-scrollbar-track {
    background-color: #333; /* Scrollbar track background */
}


/* Chat message styling */
.chat-message {
    display: flex !important; /* Use flexbox for avatar and message alignment */
    max-width: 100% !important; /* Ensure no overflow */
    word-wrap: break-word !important; /* Break long words */
    margin-bottom: 10px !important; /* Space between messages */
}

/* User and bot message backgrounds */
.chat-message.user .message {
    background-color: #2b313e !important; /* Dark background for user */
    padding: 10px !important;
    border-radius: 8px !important;
    color: #fff !important;
    margin-left: 10px !important; /* Add space from avatar */
}

.chat-message.bot .message {
    background-color: #475063 !important; /* Dark background for bot */
    padding: 10px !important;
    border-radius: 8px !important;
    color: #fff !important;
    margin-left: 10px !important; /* Add space from avatar */
}

/* Avatar styling */
.chat-message .avatar img {
    width: 35px !important; /* Avatar width */
    height: 35px !important; /* Avatar height */
    border-radius: 50% !important; /* Circular avatars */
    object-fit: cover !important; /* Keep avatar aspect ratio */
}

/* Sidebar styling */
.stSidebar {
    background-color: #262626 !important; /* Dark sidebar background */
    color: white !important; /* White sidebar text */
}

/* Sidebar headers */
.stSidebar h1, 
.stSidebar h2, 
.stSidebar h3, 
.stSidebar h4, 
.stSidebar h5, 
.stSidebar h6 {
    color: white !important; /* White sidebar headers */
}

/* Sidebar button styling */
.stSidebar button {
    background-color: white !important; /* White button color */
    color: black !important; /* Black text */
    border: 1.5px solid black; /* Black border */
    border-radius: 10px; /* Rounded edges */
    padding: 10px; /* Button padding */
    transition: background-color 0.3s ease-in-out; /* Hover transition */
}

/* Sidebar button hover effect */
.stSidebar button:hover {
    background-color: #101010 !important; /* Black on hover */
    color: white !important; /* White text on hover */
    border: 1.5px solid white; /* White border on hover */
}

/* File uploader styling */
.stSidebar .stFileUploader {
    border: 2px solid white; /* White border */
    border-radius: 10px; /* Rounded edges */
    padding: 1rem; /* Padding inside uploader */
    margin-bottom: 1.5rem; /* Space below uploader */
    background-color: #1F1F1F; /* Dark background */
    color: white; /* White text */
}

/* Drag and drop text styling */
.stSidebar .stFileUploader label {
    color: white !important; /* White text */
    font-weight: bold; /* Bold text */
    font-size: 1.3rem; /* Font size */
    text-align: center; /* Centered text */
    padding: 10px; /* Padding around text */
    display: inline-block; /* Inline block styling */
}

/* Browse files text styling */
.stSidebar .stFileUploader span {
    color: black !important; /* Black text */
}

/* Process button styling */
.stButton > button {
    background-color: #101010 !important; /* Black button background */
    color: white !important; /* White button text */
    border: 2px solid white; /* White border */
    border-radius: 10px; /* Rounded edges */
    padding: 12px; /* Padding inside button */
    font-size: 1.1rem; /* Font size */
    font-weight: bold; /* Bold text */
    margin: 1.5rem 0; /* Margin above and below */
    width: 100%; /* Full width */
    transition: background-color 0.3s ease-in-out; /* Hover transition */
}

/* Process button hover effect */
.stButton > button:hover {
    background-color: white !important; /* White on hover */
    color: black !important; /* Black text on hover */
    border: 2px solid black; /* Black border on hover */
}

/* Additional padding for sidebar sections */
.sidebar-section {
    margin-top: 20px; /* Margin above sections */
    padding: 10px; /* Padding inside sections */
    border-top: 1px solid #444; /* Top border for separation */
}

.stSidebar .sidebar-section h3 {
    margin-bottom: 10px; /* Space below section header */
    color: #f39c12; /* Orange color for section headers */
}

/* Tooltip styling */
.stTooltip {
    background-color: #333 !important; /* Dark tooltip background */
    color: white !important; /* White tooltip text */
}
</style>

'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png"> <!-- Avatar image for bot messages -->
    </div>
    <div class="message">{{MSG}}</div> <!-- Placeholder for bot messages -->
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.postimg.cc/h4V0TgqD/img1.jpg"> <!-- Avatar image for user messages -->
    </div>
    <div class="message">{{MSG}}</div> <!-- Placeholder for user messages -->
</div>
=======
css = '''
<style>
/* Global styling for the entire screen */
body {
    background-color: #303030; /* Dark grey background */
    color: white !important; /* White text color */
    font-family: 'Arial', sans-serif; /* Font family */
}

input[type="text"] {
    background-color: white !important; /* Black background */
    outline: none !important; /* Remove the default outline */
    box-shadow: none !important; /* Remove any default shadow */

}
/* Label text for input boxes */
label {
    color: white !important;
}

/* Main content area styling */
.stApp {
    background-color: #303030; /* Dark grey background */
    color: white !important; 
}

/* Header styling */
h1, h2, h3, h4, h5, h6 {
    color: white !important; /* White color for headers */
    text-align: center; /* Centered text */
    font-weight: bold; /* Bold headers */
    margin-bottom: 1rem; /* Space below headers */
}

/* Header background */
header {
    background-color: #303030 !important; /* Dark grey background */
}

.chat-message {
    padding: 0.8rem; /* Small padding */
    border-radius: 13px; /* Rounded edges */
    border: 0.5px solid white; /* No border */
    margin: 0.5rem auto; /* Center the message with space below */
    display: flex; /* Flexbox layout */
    align-items: flex-start; /* Align avatar to the top-left */
    max-width: 80%; /* Limit width */
    max-height: 200px; /* Set maximum height for the message */
    overflow-y: auto; /* Enable vertical scrolling */
}

/* User and bot message backgrounds */
.chat-message.user {
    background-color: #2b313e; /* Darker user message background */
}
.chat-message.bot {
    background-color: #475063; /* Darker bot message background */
}

/* Message text styling */
.chat-message .message {
    width: 100%; /* Full width */
    text-align: left; /* Centered text */
    color: #fff; /* White text */
    font-size: 0.9rem; /* Font size */
    padding-top: 5px !important; /* Add top padding (adjust value as needed) */

}

/* Avatar styling */
.chat-message .avatar {
    width: 10%; /* Avatar width */
    margin-right: 0.5rem; /* Space between avatar and message */
}

.chat-message .avatar img {
    max-width: 35px; /* Avatar image width */
    max-height: 35px; /* Avatar image height */
    border-radius: 50%; /* Circular avatar */
    object-fit: cover; /* Cover space without stretching */
}

/* Sidebar styling */
.stSidebar {
    background-color: #262626 !important; /* Dark sidebar background */
    color: white !important; /* White sidebar text */
}

/* Sidebar headers */
.stSidebar h1, 
.stSidebar h2, 
.stSidebar h3, 
.stSidebar h4, 
.stSidebar h5, 
.stSidebar h6 {
    color: white !important; /* White sidebar headers */
}

/* Sidebar button styling */
.stSidebar button {
    background-color: white !important; /* White button color */
    color: black !important; /* Black text */
    border: 1.5px solid black; /* Black border */
    border-radius: 10px; /* Rounded edges */
    padding: 10px; /* Button padding */
    transition: background-color 0.3s ease-in-out; /* Hover transition */
}

/* Sidebar button hover effect */
.stSidebar button:hover {
    background-color: #101010 !important; /* Black on hover */
    color: white !important; /* White text on hover */
    border: 1.5px solid white; /* White border on hover */
}

/* File uploader styling */
.stSidebar .stFileUploader {
    border: 2px solid white; /* White border */
    border-radius: 10px; /* Rounded edges */
    padding: 1rem; /* Padding inside uploader */
    margin-bottom: 1.5rem; /* Space below uploader */
    background-color: #1F1F1F; /* Dark background */
    color: white; /* White text */
}

/* Drag and drop text styling */
.stSidebar .stFileUploader label {
    color: white !important; /* White text */
    font-weight: bold; /* Bold text */
    font-size: 1.3rem; /* Font size */
    text-align: center; /* Centered text */
    padding: 10px; /* Padding around text */
    display: inline-block; /* Inline block styling */
}

/* Browse files text styling */
.stSidebar .stFileUploader span {
    color: black !important; /* Black text */
}

/* Process button styling */
.stButton > button {
    background-color: #101010 !important; /* Black button background */
    color: white !important; /* White button text */
    border: 2px solid white; /* White border */
    border-radius: 10px; /* Rounded edges */
    padding: 12px; /* Padding inside button */
    font-size: 1.1rem; /* Font size */
    font-weight: bold; /* Bold text */
    margin: 1.5rem 0; /* Margin above and below */
    width: 100%; /* Full width */
    transition: background-color 0.3s ease-in-out; /* Hover transition */
}

/* Process button hover effect */
.stButton > button:hover {
    background-color: white !important; /* White on hover */
    color: black !important; /* Black text on hover */
    border: 2px solid black; /* Black border on hover */
}

/* Additional padding for sidebar sections */
.sidebar-section {
    margin-top: 20px; /* Margin above sections */
    padding: 10px; /* Padding inside sections */
    border-top: 1px solid #444; /* Top border for separation */
}

.stSidebar .sidebar-section h3 {
    margin-bottom: 10px; /* Space below section header */
    color: #f39c12; /* Orange color for section headers */
}

/* Tooltip styling */
.stTooltip {
    background-color: #333 !important; /* Dark tooltip background */
    color: white !important; /* White tooltip text */
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png"> <!-- Avatar image for bot messages -->
    </div>
    <div class="message">{{MSG}}</div> <!-- Placeholder for bot messages -->
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.postimg.cc/h4V0TgqD/img1.jpg"> <!-- Avatar image for user messages -->
    </div>
    <div class="message">{{MSG}}</div> <!-- Placeholder for user messages -->
</div>
>>>>>>> 7f47261 (initial commit)
'''
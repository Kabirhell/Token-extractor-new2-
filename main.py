from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template as a string (simplified version of your original HTML)
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>SHAWX Token</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body, html {
      margin: 0;
      padding: 0;
      font-family: 'Roboto', sans-serif;
      background-color: #000;
      color: #28a745;
    }
    .header {
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: #1c1c1c;
      padding: 20px;
      border-bottom: 2px solid #28a745;
      margin-bottom: 20px;
    }
    .header h1 {
      margin: 0;
      font-size: 2rem;
      color: #28a745;
    }
    .header img {
      max-width: 100px;
      margin-right: 20px;
    }
    .form-container {
      background-color: #1c1c1c;
      padding: 30px;
      border-radius: 10px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
      max-width: 600px;
      margin: 20px auto;
    }
    h1, h2 {
      color: #28a745;
      text-align: center;
    }
    label {
      font-weight: bold;
      margin-bottom: 5px;
      color: #28a745;
    }
    input[type="text"] {
      width: 100%;
      padding: 10px;
      border: 1px solid #28a745;
      border-radius: 5px;
      background-color: #333;
      color: #28a745;
      margin-top: 5px;
    }
    input[type="submit"], .btn-submit {
      width: 100%;
      padding: 10px;
      background-color: #28a745;
      color: #000;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-size: 16px;
      margin-top: 10px;
      text-align: center;
      text-decoration: none;
      display: block;
    }
    input[type="submit"]:hover, .btn-submit:hover {
      background-color: #218838;
    }
    .response-box {
      border: 2px solid #28a745;
      padding: 10px;
      background-color: #333;
      border-radius: 4px;
      margin-bottom: 20px;
      width: 100%;
      word-wrap: break-word;
      text-align: center;
      color: #28a745;
      font-size: 16px;
    }
  </style>
</head>
<body>
  <header class="header">
    <div class="container text-center">
      <div class="image-container">
        <img src="https://imgur.com/bSHJtut.png" alt="Image">
      </div>
      <h1 class="mt-3">Shawx Monarch</h1>
    </div>
  </header>

  <div class="form-container">
    <h1>Facebook Access Token</h1>
    
    <h2>Enter your Facebook Cookies</h2>
    <form method="post" action="/">
      <input type="text" name="cookies" class="form-control" placeholder="Paste your Simple cookie here" required>
      <button type="submit" class="btn-submit">Get Access Token</button>
    </form>
    
    <!-- Connect Button -->
    <a href="https://www.facebook.com/dialog/oauth?scope=user_about_me%2Cuser_actions.books%2Cuser_actions.fitness%2Cuser_actions.music%2Cuser_actions.news%2Cuser_actions.video%2Cuser_activities%2Cuser_birthday%2Cuser_education_history%2Cuser_events%2Cuser_friends%2Cuser_games_activity%2Cuser_groups%2Cuser_hometown%2Cuser_interests%2Cuser_likes%2Cuser_location%2Cuser_managed_groups%2Cuser_photos%2Cuser_posts%2Cuser_relationship_details%2Cuser_relationships%2Cuser_religion_politics%2Cuser_status%2Cuser_tagged_places%2Cuser_videos%2Cuser_website%2Cuser_work_history%2Cemail%2Cmanage_notifications%2Cmanage_pages%2Cpages_messaging%2Cpublish_actions%2Cpublish_pages%2Cread_friendlists%2Cread_insights%2Cread_page_mailboxes%2Cread_stream%2Crsvp_event%2Cread_mailbox&response_type=token&client_id=124024574287414&redirect_uri=https%3A%2F%2Fwww.instagram.com%2F" class="btn-submit">Connect Instagram</a>
    
    {% if response %}
    <div class="response-box">{{ response }}</div>
    {% endif %}
  </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == 'POST':
        cookies = request.form.get('cookies')
        # Placeholder for processing cookies into an access token
        # In a real application, you'd implement logic here to convert cookies to a token
        response = f"Received cookies: {cookies} (Access token generation not implemented)"
    return render_template_string(HTML_TEMPLATE, response=response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

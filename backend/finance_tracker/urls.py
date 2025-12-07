"""
URL configuration for finance_tracker project.
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home_view(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Personal Finance Tracker - API</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }
            .container {
                background: white;
                border-radius: 24px;
                padding: 60px 40px;
                text-align: center;
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
                max-width: 500px;
                width: 100%;
            }
            .emoji {
                font-size: 80px;
                margin-bottom: 20px;
                animation: bounce 2s ease infinite;
            }
            @keyframes bounce {
                0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
                40% { transform: translateY(-20px); }
                60% { transform: translateY(-10px); }
            }
            h1 {
                color: #1a1a2e;
                font-size: 28px;
                margin-bottom: 10px;
            }
            .subtitle {
                color: #667eea;
                font-size: 18px;
                font-weight: 600;
                margin-bottom: 20px;
            }
            p {
                color: #666;
                font-size: 16px;
                line-height: 1.6;
                margin-bottom: 30px;
            }
            .highlight {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: 700;
            }
            .btn {
                display: inline-block;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 16px 40px;
                border-radius: 50px;
                text-decoration: none;
                font-weight: 600;
                font-size: 16px;
                transition: transform 0.3s, box-shadow 0.3s;
                box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
            }
            .btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 15px 30px rgba(102, 126, 234, 0.4);
            }
            .api-info {
                margin-top: 40px;
                padding-top: 30px;
                border-top: 1px solid #eee;
            }
            .api-info h3 {
                color: #333;
                font-size: 14px;
                text-transform: uppercase;
                letter-spacing: 1px;
                margin-bottom: 15px;
            }
            .endpoints {
                display: flex;
                flex-wrap: wrap;
                gap: 8px;
                justify-content: center;
            }
            .endpoint {
                background: #f0f0f0;
                padding: 6px 12px;
                border-radius: 20px;
                font-size: 12px;
                color: #555;
                font-family: monospace;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="emoji">🙈</div>
            <h1>Oops! Wrong URL</h1>
            <p class="subtitle">This is the API server</p>
            <p>
                You've reached the <span class="highlight">backend API</span> of Personal Finance Tracker. 
                The actual app with the beautiful UI lives somewhere else!
            </p>
            <a href="http://localhost:3000" class="btn" id="frontendLink">
                🚀 Go to App
            </a>
            <div class="api-info">
                <h3>📡 Available API Endpoints</h3>
                <div class="endpoints">
                    <span class="endpoint">/api/auth/login/</span>
                    <span class="endpoint">/api/auth/register/</span>
                    <span class="endpoint">/api/transactions/</span>
                    <span class="endpoint">/api/categories/</span>
                    <span class="endpoint">/api/budgets/</span>
                    <span class="endpoint">/admin/</span>
                </div>
            </div>
        </div>
        <script>
            // Auto-detect frontend URL for Codespaces
            const currentHost = window.location.hostname;
            if (currentHost.includes('app.github.dev')) {
                const frontendUrl = currentHost.replace('-8000.', '-3000.');
                document.getElementById('frontendLink').href = 'https://' + frontendUrl;
            }
        </script>
    </body>
    </html>
    """
    return HttpResponse(html)


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/', include('transactions.urls')),
    path('api/', include('budgets.urls')),
]


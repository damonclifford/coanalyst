<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your AI Partner in Analysis and Insight | coanalyst.ai</title>
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="shortcut icon" type="image/x-icon" href="{{ url_for('static', filename='images/favicon.png') }}">

    <style>
        :root {
            --primary-color: #3b82f6;
            --primary-dark: #2563eb;
            --secondary-color: #f0f9ff;
            --accent-color: #0ea5e9;
            --text-primary: #1f2937;
            --text-secondary: #6b7280;
            --border-color: #e5e7eb;
            --shadow-light: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
            --shadow-medium: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            --shadow-large: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            --gradient-primary: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
            --gradient-secondary: linear-gradient(135deg, #e0f2fe 0%, #b3e5fc 100%);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
            min-height: 100vh;
            color: var(--text-primary);
            line-height: 1.6;
        }

        .hero-section {
            background: var(--gradient-primary);
            padding: 2rem 0 3rem;
            position: relative;
            overflow: hidden;
        }

        .hero-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="white" opacity="0.05"/><circle cx="75" cy="75" r="1" fill="white" opacity="0.05"/><circle cx="50" cy="10" r="1" fill="white" opacity="0.03"/></pattern></defs><rect width="100%" height="100%" fill="url(%23grain)"/></svg>');
            pointer-events: none;
        }

        .hero-content {
            position: relative;
            z-index: 2;
        }

        .hero-title {
            font-size: 3.5rem;
            font-weight: 700;
            color: #000000;
            margin-bottom: 0.5rem;
            text-align: center;
            letter-spacing: -0.02em;
        }

        .hero-subtitle {
            font-size: 1.25rem;
            color: #000000;
            text-align: center;
            margin-bottom: 2rem;
            font-weight: 400;
        }

        .hero-badge {
            display: inline-flex;
            align-items: center;
            background: rgba(59, 130, 246, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(59, 130, 246, 0.2);
            border-radius: 50px;
            padding: 0.5rem 1rem;
            color: #000000;
            font-size: 0.875rem;
            font-weight: 500;
            margin-bottom: 1rem;
        }

        .main-card {
            background: white;
            border-radius: 24px;
            box-shadow: var(--shadow-large);
            border: 1px solid var(--border-color);
            margin-top: -3rem;
            position: relative;
            z-index: 3;
            overflow: hidden;
        }

        .card-header {
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
            border-bottom: 1px solid var(--border-color);
            padding: 2rem;
        }

        .section-title {
            font-size: 1.5rem;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .section-subtitle {
            color: var(--text-secondary);
            font-size: 1rem;
        }

        .form-section {
            padding: 2rem;
        }

        .form-label {
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 0.75rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .form-control {
            border: 2px solid var(--border-color);
            border-radius: 12px;
            padding: 0.875rem 1rem;
            font-size: 1rem;
            transition: all 0.2s ease;
            background: #fafbfc;
        }

        .form-control:focus {
            border-color: var(--primary-color);
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
            background: white;
        }

        .btn-primary {
            background: var(--primary-color);
            border: none;
            border-radius: 12px;
            padding: 0.875rem 2rem;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }

        .btn-primary:hover {
            background: var(--primary-dark);
            transform: translateY(-1px);
            box-shadow: var(--shadow-medium);
        }

        .btn-secondary {
            background: #6b7280;
            border: none;
            border-radius: 12px;
            padding: 0.875rem 2rem;
            font-weight: 600;
            font-size: 1rem;
            color: white;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }

        .btn-secondary:hover {
            background: #4b5563;
            color: white;
            transform: translateY(-1px);
            box-shadow: var(--shadow-medium);
        }

        .suggestions-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }

        .suggestion-item {
            background: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1rem;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .suggestion-item:hover {
            background: var(--primary-color);
            color: white;
            transform: translateY(-2px);
            box-shadow: var(--shadow-medium);
        }

        .data-preview {
            background: #f8fafc;
            border-radius: 16px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            border: 1px solid var(--border-color);
        }

        .table {
            margin-bottom: 0;
            border-radius: 12px;
            overflow: hidden;
            font-size: 0.875rem;
        }

        .table thead th {
            background: var(--primary-color);
            color: white;
            border: none;
            font-weight: 600;
            padding: 1rem;
        }

        .table tbody td {
            padding: 0.875rem 1rem;
            vertical-align: middle;
            border-color: var(--border-color);
        }

        .table tbody tr:hover {
            background-color: rgba(99, 102, 241, 0.05);
        }

        .results-section {
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
            border-radius: 16px;
            padding: 2rem;
            margin-top: 2rem;
            border: 1px solid var(--border-color);
        }

        .result-item {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: var(--shadow-light);
            border: 1px solid var(--border-color);
        }

        .result-item:last-child {
            margin-bottom: 0;
        }

        .result-title {
            font-size: 1.125rem;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 0.75rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .sql-query {
            background: #1f2937;
            color: #e5e7eb;
            border-radius: 8px;
            padding: 1rem;
            font-family: 'Courier New', monospace;
            font-size: 0.875rem;
            overflow-x: auto;
        }

        .footer {
            background: #f8f9fa;
            color: #6b7280;
            padding: 3rem 0 2rem;
            margin-top: 4rem;
            border-top: 1px solid #e5e7eb;
        }

        .footer-content {
            text-align: center;
        }

        .footer-links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
        }

        .footer-links a {
            color: #6b7280;
            text-decoration: none;
            transition: color 0.2s ease;
        }

        .footer-links a:hover {
            color: #374151;
        }

        .copyright {
            color: #9ca3af;
            font-size: 0.875rem;
        }

        @media (max-width: 768px) {
            .hero-title {
                font-size: 2.5rem;
            }
            
            .hero-subtitle {
                font-size: 1.125rem;
            }
            
            .main-card {
                margin: 1rem;
                border-radius: 16px;
            }
            
            .suggestions-grid {
                grid-template-columns: 1fr;
            }
            
            .table {
                font-size: 0.75rem;
            }
            
            .table thead th,
            .table tbody td {
                padding: 0.5rem;
            }
        }

        .fade-in {
            animation: fadeIn 0.6s ease-out;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .loading {
            display: none;
            align-items: center;
            gap: 0.5rem;
            color: var(--text-secondary);
        }

        .loading.active {
            display: flex;
        }

        .spinner {
            width: 16px;
            height: 16px;
            border: 2px solid var(--border-color);
            border-top: 2px solid var(--primary-color);
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <!-- Hero Section -->
    <section class="hero-section">
        <div class="container hero-content">
            <div class="row justify-content-center">
                <div class="col-lg-8 text-center">
                    <h1 class="hero-title">coanalyst.ai</h1>
                    <div class="hero-badge">
                        <i class="fas fa-sparkles me-2"></i>
                        Version 0.5 - AI-Powered Analytics
                    </div>
                    <p class="hero-subtitle">Transform your data into insights with natural language queries powered by advanced AI</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Main Content -->
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-10">
                <div class="main-card fade-in">
                    <div class="card-header">
                        <h2 class="section-title">
                            <i class="fas fa-brain text-primary"></i>
                            AI Data Analysis
                        </h2>
                        <p class="section-subtitle">Ask questions about your data in plain English and get instant insights</p>
                    </div>

                    <div class="form-section">
                        <form method="post" id="analysisForm">
                            <!-- Question Input -->
                            <div class="mb-4">
                                <label for="question" class="form-label">
                                    <i class="fas fa-question-circle text-primary"></i>
                                    What question do you have about the data?
                                </label>
                                <input type="text" 
                                       id="question" 
                                       name="question" 
                                       class="form-control" 
                                       placeholder="e.g., What was the total revenue?" 
                                       required>
                            </div>

                            <!-- Suggestions -->
                            <div class="mb-4">
                                <label class="form-label">
                                    <i class="fas fa-lightbulb text-warning"></i>
                                    Try these example questions:
                                </label>
                                <div class="suggestions-grid">
                                    <div class="suggestion-item" onclick="fillQuestion('What was the total revenue?')">
                                        <i class="fas fa-dollar-sign"></i>
                                        What was the total revenue?
                                    </div>
                                    <div class="suggestion-item" onclick="fillQuestion('What were the top two stores and their sales?')">
                                        <i class="fas fa-store"></i>
                                        Top performing stores
                                    </div>
                                    <div class="suggestion-item" onclick="fillQuestion('Who was the top customer?')">
                                        <i class="fas fa-user-tie"></i>
                                        Top customer analysis
                                    </div>
                                    <div class="suggestion-item" onclick="fillQuestion('How much did the Miami store sell?')">
                                        <i class="fas fa-map-marker-alt"></i>
                                        Store-specific sales
                                    </div>
                                    <div class="suggestion-item" onclick="fillQuestion('What is the average order value?')">
                                        <i class="fas fa-calculator"></i>
                                        Average order value
                                    </div>
                                    <div class="suggestion-item" onclick="fillQuestion('Which products sell the most by quantity?')">
                                        <i class="fas fa-chart-bar"></i>
                                        Best selling products
                                    </div>
                                </div>
                            </div>

                            <!-- Data Preview -->
                            <div class="mb-4">
                                <label class="form-label">
                                    <i class="fas fa-table text-info"></i>
                                    Data Preview (UCI Online Retail Dataset)
                                </label>
                                <div class="data-preview">
                                    <div class="table-responsive">
                                        <table class="table table-hover">
                                            <thead>
                                                <tr>
                                                    <th>InvoiceNo</th>
                                                    <th>StockCode</th>
                                                    <th>Description</th>
                                                    <th>Quantity</th>
                                                    <th>InvoiceDate</th>
                                                    <th>UnitPrice</th>
                                                    <th>CustomerID</th>
                                                    <th>Store</th>
                                                    <th>CustomerName</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr>
                                                    <td>536365</td>
                                                    <td>85123A</td>
                                                    <td>WHITE HANGING HEART T-LIGHT HOLDER</td>
                                                    <td>6</td>
                                                    <td>12/01/2020</td>
                                                    <td>2.55</td>
                                                    <td>17850</td>
                                                    <td>Tampa</td>
                                                    <td>Emma</td>
                                                </tr>
                                                <tr>
                                                    <td>536365</td>
                                                    <td>71053</td>
                                                    <td>WHITE METAL LANTERN</td>
                                                    <td>6</td>
                                                    <td>12/01/2020</td>
                                                    <td>3.39</td>
                                                    <td>17850</td>
                                                    <td>Tampa</td>
                                                    <td>Emma</td>
                                                </tr>
                                                <tr>
                                                    <td>536365</td>
                                                    <td>84406B</td>
                                                    <td>CREAM CUPID HEARTS COAT HANGER</td>
                                                    <td>8</td>
                                                    <td>12/01/2020</td>
                                                    <td>2.75</td>
                                                    <td>17850</td>
                                                    <td>Tampa</td>
                                                    <td>Emma</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>

                            <!-- Submit Button -->
                            <div class="mb-3">
                                <button type="submit" class="btn btn-primary me-3">
                                    <i class="fas fa-search"></i>
                                    Analyze Data
                                </button>
                                <button type="button" class="btn btn-secondary" onclick="resetForm()">
                                    <i class="fas fa-undo"></i>
                                    Reset
                                </button>
                                <div class="loading ms-3" id="loadingIndicator">
                                    <div class="spinner"></div>
                                    Processing your query...
                                </div>
                            </div>
                        </form>

                        <!-- Results Section -->
                        {% if response %}
                        <div class="results-section fade-in">
                            <div class="result-item">
                                <h4 class="result-title">
                                    <i class="fas fa-question-circle text-primary"></i>
                                    Your Question
                                </h4>
                                <p class="mb-0">{{ question }}</p>
                            </div>

                            <div class="result-item">
                                <h4 class="result-title">
                                    <i class="fas fa-database text-info"></i>
                                    Generated SQL Query
                                </h4>
                                <div class="sql-query">{{ query }}</div>
                            </div>

                            <div class="result-item">
                                <h4 class="result-title">
                                    <i class="fas fa-chart-line text-success"></i>
                                    AI Analysis
                                </h4>
                                <p class="mb-0">{{ response }}</p>
                            </div>
                        </div>
                        {% endif %}

                        {% if error %}
                        <div class="alert alert-danger fade-in" role="alert">
                            <i class="fas fa-exclamation-triangle me-2"></i>
                            {{ error }}
                        </div>
                        {% endif %}
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-links">
                    <a href="https://github.com/damonclifford/coanalyst">
                        <i class="fab fa-github me-1"></i>
                        GitHub Repository
                    </a>
                    <a href="https://www.contentgeneration.io/">
                        <i class="fas fa-tools me-1"></i>
                        AI Content Tools
                    </a>
                </div>
                <p class="copyright">
                    &copy; 2023 coanalyst.ai. All Rights Reserved.
                </p>
            </div>
        </div>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <script>
        function fillQuestion(question) {
            document.getElementById('question').value = question;
            document.getElementById('question').focus();
        }

        function resetForm() {
            // Clear the form
            document.getElementById('analysisForm').reset();
            
            // Hide loading indicator
            document.getElementById('loadingIndicator').classList.remove('active');
            
            // Remove results section and error messages
            const resultsSection = document.querySelector('.results-section');
            if (resultsSection) {
                resultsSection.remove();
            }
            
            const errorAlert = document.querySelector('.alert-danger');
            if (errorAlert) {
                errorAlert.remove();
            }
            
            // Scroll back to the top of the form
            document.getElementById('question').scrollIntoView({ 
                behavior: 'smooth', 
                block: 'center' 
            });
            
            // Focus on the question input
            setTimeout(() => {
                document.getElementById('question').focus();
            }, 500);
        }

        document.getElementById('analysisForm').addEventListener('submit', function() {
            document.getElementById('loadingIndicator').classList.add('active');
        });

        // Add smooth scrolling to results
        {% if response %}
        setTimeout(() => {
            document.querySelector('.results-section').scrollIntoView({ 
                behavior: 'smooth', 
                block: 'start' 
            });
        }, 100);
        {% endif %}
    </script>

</body>
</html>

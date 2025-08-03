Clone the github repo and open the folder FocusMate

Create an empty folders inside the FocusMate folder: data, outputs

Module-1: User Activity & App Monitoring
1) Initiate the virtual environment: python -m venv venv
2) Connect to venv: .\venv\Scripts\Activate.ps1
3) Now install the packages: pip install -r requirements.txt
4) Now run Module-1: python -m module_1_activity_monitor.main

Module-2: Data Preprocessing & Storage
1) install the packages: pip install pandas
2) To run: python -m module_1_activity_monitor.preprocess

Module-3: Focus Pattern Analysis (Unsupervised ML)
To run: python run_analysis.py

Module-4: Personalized Recommendations (AI Assistant)
1) create a .env file in FocusMate folder and copy the code: OPENROUTER_API_KEY=YOUR_API_KEY
2) Import the package: pip install opanai
3) To run: python run_assistant.py

Module-5: Dashboard & Visualization
1) Import the packages: pip install streamlit plotly
2) To run: streamlit run dashboard/app.py

Module-6: Focus Mode + Smart Blocking (Optional Add-on)
1) Import the package: pip install plyer
2) To run: python run_focus_mode.py

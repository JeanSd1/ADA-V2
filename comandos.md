comandos 
ption 1: The "Easy" Way (Single Terminal)
The app is smart enough to start the backend for you.

Open your terminal in the ada_v2 folder.
Activate your environment: conda activate ada_v2
Run:
npm run dev
The backend will start automatically in the background.
Option 2: The "Developer" Way (Two Terminals)
Use this if you want to see the Python logs (recommended for debugging).

Terminal 1 (Backend):

conda activate ada_v2
python backend/server.py
Terminal 2 (Frontend):

# Environment doesn't matter here, but keep it simple
npm run dev

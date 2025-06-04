from pyngrok import ngrok
import uvicorn
import nest_asyncio
import threading

# Apply Nest Asyncio to run in notebook cell
nest_asyncio.apply()

def run():
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

# Start ngrok tunnel
public_url = ngrok.connect(8000)
print(f"🚀 Your API is live at: {public_url}")

# Start server in a separate thread
threading.Thread(target=run).start()

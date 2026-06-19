import azure.functions as func

app = func.FunctionApp()

@app.timer_trigger(
    schedule="0 0 2 * * *",
    arg_name="timer",
    run_on_startup=True
)
def pocket_sync(timer: func.TimerRequest):
    print("Pocket sync started")
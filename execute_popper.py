import json
import os
from popper.util import Settings
from popper.loop import learn_solution
from popper.util import format_prog 

# Load settings.json
with open("settings.json", "r") as f:
    settings_json = json.load(f)

# Extract folder path and Popper settings
experiment_name = settings_json.get("experiment_name", "default_exp")
kbpath = os.path.join("input_data", experiment_name)
results_file = os.path.join(kbpath, "results.txt")

popper_settings = settings_json.get("popper_settings", {})

# Ensure defaults if not specified
settings = Settings(
    kbpath=kbpath,
    max_rules=popper_settings.get("max_rules", 3),
    max_literals=popper_settings.get("max_literals", 6),
    timeout=popper_settings.get("timeout", 1200),
    noisy=popper_settings.get("noisy", True),
    show_stats=popper_settings.get("show_stats", True),
    debug=popper_settings.get("debug", False),
)

# Ensure the results directory exists
os.makedirs(kbpath, exist_ok=True)

try:
    prog, score, stats = learn_solution(settings)
    
    with open(results_file, "w") as f:
        f.write(f"Tried {stats.total_programs} programs\n")
        
        if prog:
            results = format_prog(prog)  # Corrected function to format the program
            f.write(f"\nLearned Program:\n{results}\n")
            f.write(f"\nScore: {score}\n")
            print(f"Results saved in {results_file}")
        else:
            f.write("\nERROR: No program was learned\n")
            print("ERROR: No program was learned")

    # Append full settings at the end
    with open(results_file, "a") as f:
        f.write("\n\n===== Settings Used =====\n")
        f.write(json.dumps(settings_json, indent=4))

except Exception as e:
    error_message = f"Popper Crashed with Error: {e}"
    print(error_message)
    
    # Save error message to the results file
    with open(results_file, "w") as f:
        f.write(error_message)

    # Append settings even if there's an error
    with open(results_file, "a") as f:
        f.write("\n\n===== Settings Used =====\n")
        f.write(json.dumps(settings_json, indent=4))

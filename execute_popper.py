import json
import os
from popper.util import Settings
from popper.loop import learn_solution
from popper.util import format_prog, order_prog, format_rule

with open("settings.json", "r") as f:
    settings_json = json.load(f)

experiment_name = settings_json.get("experiment_name", "default_exp")
kbpath = os.path.join("input_data", experiment_name)
results_file = os.path.join(kbpath, "results.txt")

popper_settings = settings_json.get("popper_settings", {})
settings = Settings(
    kbpath=kbpath,
    max_rules=popper_settings.get("max_rules", 3),
    max_literals=popper_settings.get("max_literals", 6),
    timeout=popper_settings.get("timeout", 1200),
    noisy=popper_settings.get("noisy", True),
    show_stats=popper_settings.get("show_stats", True),
    debug=popper_settings.get("debug", False),
)

os.makedirs(kbpath, exist_ok=True)

try:
    prog, score, stats = learn_solution(settings)
    
    with open(results_file, "w") as f:
        f.write(f"Tried {stats.total_programs} programs\n")
        
        if prog:
            tp, fn, tn, fp, size = score
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0
            mdl = size + fn + fp

            f.write(f"\nPrecision:{precision:.2f} Recall:{recall:.2f} TP:{tp} FN:{fn} TN:{tn} FP:{fp} Size:{size} MDL:{mdl} --rules\n")

            for rule in order_prog(prog):
                f.write(format_rule(rule) + "\n")

            print(f"Results saved in {results_file}")
        else:
            f.write("\nERROR: No program was learned\n")
            print("ERROR: No program was learned")

    with open(results_file, "a") as f:
        f.write("\n\n===== Settings Used =====\n")
        f.write(json.dumps(settings_json, indent=4))

except Exception as e:
    error_message = f"Popper Crashed with Error: {e}"
    print(error_message)
    
    with open(results_file, "w") as f:
        f.write(error_message)

    with open(results_file, "a") as f:
        f.write("\n\n===== Settings Used =====\n")
        f.write(json.dumps(settings_json, indent=4))

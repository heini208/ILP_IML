from popper.util import Settings
from popper.loop import learn_solution

settings = Settings(
    kbpath='input_data/loan_approval_complete',
    max_rules=5, 
    max_literals=5,  
    max_body=6,  
    max_vars=6,  
    show_stats=True,
    noisy=True
)

try:
    prog, score, stats = learn_solution(settings)
    print(f"Tried {stats.total_programs} programs")
    if prog:
        settings.print_prog_score(prog, score)
    else:
        print("❌ ERROR: No program was learned")
except Exception as e:
    print(f"⚠️ Popper Crashed with Error: {e}")

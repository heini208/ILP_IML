from popper.util import Settings
from popper.loop import learn_solution

settings = Settings(kbpath='input_data/example')
prog, score, stats = learn_solution(settings)
if prog:
    settings.print_prog_score(prog, score)
    

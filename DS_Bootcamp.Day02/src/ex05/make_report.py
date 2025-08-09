import sys
from analytics import Research, Analytics, Calculations
import config

if len(sys.argv) != 2:
    print("Usage: python3 make_report.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    research = Research(file_path)
    data = research.file_reader(has_header=True)
    
    calc = Calculations(data)
    head_count, tail_count = calc.counts()
    head_frac, tail_frac = calc.fractions((head_count, tail_count))
    
    analytics = Analytics(data)
    predictions = analytics.predict_random(config.NUM_OF_STEPS)
    
    pred_head = sum(1 for pred in predictions if pred[0] == 1)
    pred_tail = sum(1 for pred in predictions if pred[1] == 1)
    
    total_observations = len(data)
    
    report = config.REPORT_TEMPLATE.format(
        total=total_observations,
        tail_count=tail_count,
        head_count=head_count,
        tail_frac=tail_frac,
        head_frac=head_frac,
        num_steps=config.NUM_OF_STEPS,
        forecast_tail=pred_tail,
        forecast_head=pred_head
    )
    
    analytics.save_file(report, "report", "txt")
    
    print(report)
except Exception as e:
    print("Error:", e)

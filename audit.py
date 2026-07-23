import argparse, json
from pathlib import Path

def audit(items):
    findings=[]
    for i in items:
        codes=[]
        if not i.get("source_segment_id"): codes.append("missing_source")
        if not i.get("owner"): codes.append("missing_owner")
        if i.get("due_date") and i["due_date"] < i["meeting_date"]: codes.append("due_before_meeting")
        if i.get("confidence",0) < 0.7 and i.get("auto_dispatch"): codes.append("low_confidence_dispatch")
        findings.append({"action_id":i["action_id"],"status":"review" if codes else "ready","codes":codes})
    return {"actions":findings,"review_count":sum(x["status"]=="review" for x in findings)}
def main():
    p=argparse.ArgumentParser(); p.add_argument("input"); p.add_argument("-o","--output",default="report.json"); a=p.parse_args()
    r=audit(json.loads(Path(a.input).read_text())["actions"]); Path(a.output).write_text(json.dumps(r,indent=2)); print(json.dumps(r,indent=2)); raise SystemExit(2 if r["review_count"] else 0)
if __name__=="__main__": main()

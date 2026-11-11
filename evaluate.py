import csv
from pathlib import Path
from detect import analyze_leaf

TEST_DIR = Path("test_images")
MIME = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png"}

rows = []

for true_label in ["healthy", "diseased"]:
    for image_path in sorted((TEST_DIR / true_label).iterdir()):
        mime = MIME.get(image_path.suffix.lower())
        if mime is None:
            continue  # skip files that are not images

        try:
            result = analyze_leaf(image_path.read_bytes(), mime)
        except Exception as error:
            print("Failed:", image_path.name, error)
            continue

        if not result.get("valid_leaf"):
            predicted = "rejected"
        elif result.get("disease_detected"):
            predicted = "diseased"
        else:
            predicted = "healthy"

        rows.append({
            "image": image_path.name,
            "true": true_label,
            "predicted": predicted,
            "disease_name": result.get("disease_name"),
            "correct": predicted == true_label,
        })
        print(image_path.name, "| true:", true_label, "| predicted:", predicted)

# Summary
total = len(rows)
correct = sum(1 for r in rows if r["correct"])
print()
print(f"Correct: {correct} of {total}")
if total:
    print(f"Accuracy: {correct / total * 100:.1f}%")

for label in ["healthy", "diseased"]:
    group = [r for r in rows if r["true"] == label]
    group_correct = sum(1 for r in group if r["correct"])
    print(f"{label}: {group_correct} of {len(group)} correct")

# Save the details for your report
with open("results.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["image", "true", "predicted", "disease_name", "correct"])
    writer.writeheader()
    writer.writerows(rows)
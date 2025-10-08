
import time

def generate_variant(name, description, generation_time_est=15):
    print(f"Generating {name} variant...")
    time.sleep(2)
    print(f"Description: {description}")
    print(f"Estimated generation time: {generation_time_est} minutes\n")

if __name__ == "__main__":
    variants = {
        "Erratic Motion": "Unstable trajectory to test behavioral predictability and trust perception.",
        "Massive Form": "Scaled morphology for dominance and spatial perception study.",
        "Signal-Rich": "Expressive lighting and cues for communicative design evaluation."
    }
    for v, d in variants.items():
        generate_variant(v, d)

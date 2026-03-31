from django.core.management.base import BaseCommand
from decisioning.models import Category, Question, AllowedAnswer

SEED_DATA = [
    {
        "name": "Career Decision",
        "description": "Evaluate career choices based on growth, salary, balance, and alignment with your goals.",
        "icon": "briefcase",
        "questions": [
            {
                "text": "How strong is the long-term career growth potential?",
                "order": 1,
                "options": [
                    {"label": "Very High", "value": 5},
                    {"label": "High", "value": 4},
                    {"label": "Moderate", "value": 3},
                    {"label": "Low", "value": 2},
                    {"label": "Very Low", "value": 1},
                ],
            },
            {
                "text": "How competitive is the salary and compensation package?",
                "order": 2,
                "options": [
                    {"label": "Excellent", "value": 5},
                    {"label": "Good", "value": 4},
                    {"label": "Average", "value": 3},
                    {"label": "Below Average", "value": 2},
                    {"label": "Poor", "value": 1},
                ],
            },
            {
                "text": "How well does this option support work-life balance?",
                "order": 3,
                "options": [
                    {"label": "Excellent", "value": 5},
                    {"label": "Good", "value": 4},
                    {"label": "Moderate", "value": 3},
                    {"label": "Poor", "value": 2},
                    {"label": "Very Poor", "value": 1},
                ],
            },
            {
                "text": "How closely does it align with your personal values and passions?",
                "order": 4,
                "options": [
                    {"label": "Perfectly", "value": 5},
                    {"label": "Strongly", "value": 4},
                    {"label": "Somewhat", "value": 3},
                    {"label": "Barely", "value": 2},
                    {"label": "Not at all", "value": 1},
                ],
            },
            {
                "text": "How stable is the company or industry?",
                "order": 5,
                "options": [
                    {"label": "Very Stable", "value": 5},
                    {"label": "Stable", "value": 4},
                    {"label": "Somewhat Stable", "value": 3},
                    {"label": "Unstable", "value": 2},
                    {"label": "Very Unstable", "value": 1},
                ],
            },
        ],
    },
    {
        "name": "Financial Investment",
        "description": "Compare investment options based on return, risk, liquidity, and time horizon.",
        "icon": "chart-line",
        "questions": [
            {
                "text": "What is the expected return on investment (ROI)?",
                "order": 1,
                "options": [
                    {"label": "Very High (>20%)", "value": 5},
                    {"label": "High (10-20%)", "value": 4},
                    {"label": "Moderate (5-10%)", "value": 3},
                    {"label": "Low (1-5%)", "value": 2},
                    {"label": "Minimal (<1%)", "value": 1},
                ],
            },
            {
                "text": "How manageable is the risk level?",
                "order": 2,
                "options": [
                    {"label": "Very Low Risk", "value": 5},
                    {"label": "Low Risk", "value": 4},
                    {"label": "Moderate Risk", "value": 3},
                    {"label": "High Risk", "value": 2},
                    {"label": "Very High Risk", "value": 1},
                ],
            },
            {
                "text": "How liquid is the investment (can you access funds quickly)?",
                "order": 3,
                "options": [
                    {"label": "Highly Liquid", "value": 5},
                    {"label": "Liquid", "value": 4},
                    {"label": "Moderately Liquid", "value": 3},
                    {"label": "Illiquid", "value": 2},
                    {"label": "Very Illiquid", "value": 1},
                ],
            },
            {
                "text": "How well does it fit your investment time horizon?",
                "order": 4,
                "options": [
                    {"label": "Perfect Fit", "value": 5},
                    {"label": "Good Fit", "value": 4},
                    {"label": "Acceptable", "value": 3},
                    {"label": "Poor Fit", "value": 2},
                    {"label": "No Fit", "value": 1},
                ],
            },
        ],
    },
    {
        "name": "Technology & Tools",
        "description": "Compare software, platforms, or tools based on cost, ease of use, and scalability.",
        "icon": "laptop-code",
        "questions": [
            {
                "text": "How affordable is the total cost of ownership?",
                "order": 1,
                "options": [
                    {"label": "Free / Very Low Cost", "value": 5},
                    {"label": "Affordable", "value": 4},
                    {"label": "Moderate Cost", "value": 3},
                    {"label": "Expensive", "value": 2},
                    {"label": "Very Expensive", "value": 1},
                ],
            },
            {
                "text": "How easy is it for the team to learn and use?",
                "order": 2,
                "options": [
                    {"label": "Very Easy", "value": 5},
                    {"label": "Easy", "value": 4},
                    {"label": "Moderate", "value": 3},
                    {"label": "Difficult", "value": 2},
                    {"label": "Very Difficult", "value": 1},
                ],
            },
            {
                "text": "How well does it scale as your project grows?",
                "order": 3,
                "options": [
                    {"label": "Scales Excellently", "value": 5},
                    {"label": "Scales Well", "value": 4},
                    {"label": "Scales Moderately", "value": 3},
                    {"label": "Limited Scaling", "value": 2},
                    {"label": "Does Not Scale", "value": 1},
                ],
            },
            {
                "text": "How active is the community and support ecosystem?",
                "order": 4,
                "options": [
                    {"label": "Very Active", "value": 5},
                    {"label": "Active", "value": 4},
                    {"label": "Moderate", "value": 3},
                    {"label": "Limited", "value": 2},
                    {"label": "Inactive", "value": 1},
                ],
            },
        ],
    },
    {
        "name": "Personal Life Choice",
        "description": "Evaluate major life decisions like relocation, education, or relationships.",
        "icon": "heart",
        "questions": [
            {
                "text": "How much does this choice align with your long-term happiness?",
                "order": 1,
                "options": [
                    {"label": "Strongly Aligned", "value": 5},
                    {"label": "Aligned", "value": 4},
                    {"label": "Neutral", "value": 3},
                    {"label": "Misaligned", "value": 2},
                    {"label": "Strongly Misaligned", "value": 1},
                ],
            },
            {
                "text": "How will this affect your key relationships?",
                "order": 2,
                "options": [
                    {"label": "Very Positively", "value": 5},
                    {"label": "Positively", "value": 4},
                    {"label": "Neutrally", "value": 3},
                    {"label": "Negatively", "value": 2},
                    {"label": "Very Negatively", "value": 1},
                ],
            },
            {
                "text": "How manageable is the financial impact of this choice?",
                "order": 3,
                "options": [
                    {"label": "No Financial Strain", "value": 5},
                    {"label": "Minor Strain", "value": 4},
                    {"label": "Moderate Strain", "value": 3},
                    {"label": "Significant Strain", "value": 2},
                    {"label": "Severe Strain", "value": 1},
                ],
            },
            {
                "text": "How reversible is this decision if things don't work out?",
                "order": 4,
                "options": [
                    {"label": "Easily Reversible", "value": 5},
                    {"label": "Reversible", "value": 4},
                    {"label": "Somewhat Reversible", "value": 3},
                    {"label": "Difficult to Reverse", "value": 2},
                    {"label": "Irreversible", "value": 1},
                ],
            },
            {
                "text": "How well does this align with your core values?",
                "order": 5,
                "options": [
                    {"label": "Perfect Alignment", "value": 5},
                    {"label": "Strong Alignment", "value": 4},
                    {"label": "Some Alignment", "value": 3},
                    {"label": "Little Alignment", "value": 2},
                    {"label": "No Alignment", "value": 1},
                ],
            },
        ],
    },
    {
        "name": "Product or Business Idea",
        "description": "Evaluate startup ideas, business plans, or product features for market viability.",
        "icon": "lightbulb",
        "questions": [
            {
                "text": "How large and reachable is the target market?",
                "order": 1,
                "options": [
                    {"label": "Massive & Easy to Reach", "value": 5},
                    {"label": "Large & Reachable", "value": 4},
                    {"label": "Moderate", "value": 3},
                    {"label": "Niche & Hard to Reach", "value": 2},
                    {"label": "Too Small", "value": 1},
                ],
            },
            {
                "text": "How strong is the revenue potential?",
                "order": 2,
                "options": [
                    {"label": "Extremely High", "value": 5},
                    {"label": "High", "value": 4},
                    {"label": "Moderate", "value": 3},
                    {"label": "Low", "value": 2},
                    {"label": "Very Low", "value": 1},
                ],
            },
            {
                "text": "How difficult is it for competitors to copy or replace?",
                "order": 3,
                "options": [
                    {"label": "Very Hard to Copy", "value": 5},
                    {"label": "Hard to Copy", "value": 4},
                    {"label": "Moderate Barrier", "value": 3},
                    {"label": "Easy to Copy", "value": 2},
                    {"label": "No Barrier at All", "value": 1},
                ],
            },
            {
                "text": "How feasible is it to build with current resources?",
                "order": 4,
                "options": [
                    {"label": "Very Feasible", "value": 5},
                    {"label": "Feasible", "value": 4},
                    {"label": "Somewhat Feasible", "value": 3},
                    {"label": "Challenging", "value": 2},
                    {"label": "Not Feasible", "value": 1},
                ],
            },
        ],
    },
]


class Command(BaseCommand):
    help = "Seeds the database with initial Categories, Questions, and AllowedAnswers."

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Delete all existing categories before seeding.",
        )

    def handle(self, *args, **options):
        if options["reset"]:
            count, _ = Category.objects.all().delete()
            self.stdout.write(self.style.WARNING(f"Deleted {count} existing category records."))

        created_count = 0
        skipped_count = 0

        for cat_data in SEED_DATA:
            category, created = Category.objects.get_or_create(
                name=cat_data["name"],
                defaults={
                    "description": cat_data["description"],
                    "icon": cat_data["icon"],
                },
            )

            if not created:
                skipped_count += 1
                self.stdout.write(f"  Skipped (already exists): {category.name}")
                continue

            created_count += 1
            for q_data in cat_data["questions"]:
                question = Question.objects.create(
                    category=category,
                    text=q_data["text"],
                    order=q_data["order"],
                )
                for opt_data in q_data["options"]:
                    AllowedAnswer.objects.create(
                        question=question,
                        label=opt_data["label"],
                        value=opt_data["value"],
                    )

            self.stdout.write(self.style.SUCCESS(f"  ✓ Created: {category.name}"))

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS(
            f"Seeding complete! Created: {created_count}, Skipped: {skipped_count}"
        ))
        self.stdout.write(self.style.SUCCESS(
            "Your frontend team can now fetch categories from GET /api/categories/"
        ))

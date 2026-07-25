# Evaluation Results

| # | Question | Retrieval (expected/actual) | Keywords OK | Pass | Cost | Latency (ms) |
|---|---|---|---|---|---|---|
| 1 | What elements does the syllabus checklist require? | True/True (x1) | True | PASS | $0.1622 | 13256 |
| 2 | What technology do law students need to bring to class? | True/True (x1) | True | PASS | $0.0644 | 7084 |
| 3 | What should instructors tell students about reporting sexual harassment? | True/True (x2) | True | PASS | $0.0862 | 16441 |
| 4 | What is the late-assignment penalty policy? | True/True (x2) | True | PASS | $0.0941 | 14702 |
| 5 | What is the capital of France? | False/False (x0) | True | PASS | $0.0347 | 4742 |
| 6 | Write a haiku about autumn. | False/False (x0) | True | PASS | $0.0296 | 1858 |

**Summary:** 6/6 passed, total cost $0.4712, average latency 9680 ms.

## Full answers

Read these manually too -- the keyword checks above are a shortcut, not proof of correctness (e.g. case 4 has no keyword check since it tests whether the agent honestly says the syllabus doesn't specify a late-assignment policy, instead of guessing).

**1. What elements does the syllabus checklist require?**

Based on the course materials, the **Syllabus Checklist** (used when submitting course syllabi with Form A, B, or C) requires that you include all of the following elements:

- **Course Title**
- **Course Number**
- **Course Credits**
- **Course Description**
- **Course Goals**
- **Student Learning Outcomes** — these must be *specific, measurable* outcomes describing what students will be able to do at the end of the course
- **Textbook and Supplies**
- **Course Requirements** — all assessable requirements that lead to a grade, specifying how much each is worth (percentages/points must add to 100% or the stated total)
- **Grading** — detailing how the grade is calculated, with a percentage breakdown using fractionalized grades
- **Graduate vs. Undergraduate Grading** — *if* the course allows both graduate and undergraduate credit, describe requirements and grading criteria for both levels
- **Accommodation Statement**
- **Schedule of Activities** — a representative course schedule is required (specific instructor/class meeting times and locations are not needed in the example syllabi)

The checklist is meant to ensure you've included all required elements before submission.

(Source: sample-syllabus.pdf, page 7)

Note: the retrieved passage for the "Schedule of Activities" entry was cut off, so there may be a small amount of additional detail (or possibly further items) on that page that I couldn't fully see. If you'd like, I can search again to confirm nothing follows it.

**2. What technology do law students need to bring to class?**

I'll search the course materials for this information.According to the course materials, law students are required to bring their **laptop** to class to follow along with or complete in-class research exercises.

Specifically:
- UNM Law School requires that all entering students own a laptop computer.
- The law school does not require a particular brand, but has determined a **minimum hardware configuration**.
- For more details, students are directed to the Law School's IT Services page (laptop program).

(Source: sample-syllabus.pdf, page 2)

**3. What should instructors tell students about reporting sexual harassment?**

Based on the course materials, here is what instructors should communicate to students regarding reporting sexual harassment (drawn from the sample syllabus's **Title IX Statement**):

## Key points instructors should tell students

1. **Faculty, TAs, and GAs are "responsible employees."** Under Title IX and the U.S. Department of Education's guidance, faculty members, Teaching Assistants, and Graduate Assistants are designated as "responsible employees." Students should know that these individuals are **not** confidential resources.

2. **Reports will be forwarded to the Title IX Coordinator.** Any report of gender discrimination — which includes **sexual harassment, sexual misconduct, and sexual violence** — that a student makes to a faculty member, TA, or GA **must** be reported to the Title IX Coordinator at the **Office of Equal Opportunity (oeo.unm.edu)**. Students should be told this up front so they understand what happens when they disclose.

3. **Where to find the full policy.** Students can read the campus policy regarding sexual misconduct at:
   `https://policy.unm.edu/university-policies/2000/2740.html`

4. **Where to get confidential help/support.** If a student has experienced sexual violence or sexual misconduct, they can ask a faculty or staff member for help, or contact the **LoboRESPECT Advocacy Center** for support.

The syllabus offers two suggested wordings for this statement, and notes that there is no single required University language — departments, schools, colleges, or campuses may have their own preferred wording, so instructors should check their unit's requirements.

(Source: sample-syllabus.pdf, page 3)

**4. What is the late-assignment penalty policy?**

I'll search the course materials for the late-assignment penalty policy.Let me search with different phrasing to check for a specific point-deduction policy.Based on the course materials, there isn't a point-based late penalty (like "X points deducted per day"). The syllabus takes a stricter stance:

**Late-assignment policy:** All assignments close at the listed due date and **will not be accepted late** — unless the circumstances are discussed and negotiated with the instructor **well ahead of the due date**.

Additionally, unless otherwise announced, all assignments (including discussion posts) are due on **Sundays by 11:59 p.m. (midnight)** for that week.

A couple of caveats worth noting:
- This wording appears in the syllabus as an *example* policy ("Example 3"), so the exact rule may vary by the specific instructor/course.
- The materials do **not** describe any graduated point-deduction scheme for late work — the only stated approach is non-acceptance with prior-negotiation as the sole exception.

(Source: sample-syllabus.pdf, page 5)

**5. What is the capital of France?**

The capital of France is **Paris**.

Note: This is general knowledge, not something drawn from your course materials, so there's no course source to cite here. If you have a France- or geography-related question that's actually part of your course content, let me know and I'll search the ingested materials for it.

**6. Write a haiku about autumn.**

Autumn leaves drifting—
crimson whispers on the wind,
earth breathes in the cold.

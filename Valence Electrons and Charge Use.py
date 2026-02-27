import streamlit as st

st.set_page_config(page_title="Valence Electrons and Oxidation States Quiz")

st.title("Valence Electrons and Oxidation States")
st.write("Select the best answer for each question. No answers are preselected.")

# ---------------------------------------------------------
# QUIZ DATA — ANSWER POSITIONS NOW VARY
# ---------------------------------------------------------
questions = [
    ("The Lewis symbol for nitrogen has:",
     ["one pair of electrons and three lone electrons",
      "two pairs of electrons and two lone electrons",
      "four lone electrons and zero pairs"],
     "one pair of electrons and three lone electrons"),

    ("The Lewis symbol for Xe has:",
     ["2 pairs of electrons",
      "4 pairs of electrons",
      "6 pairs of electrons"],
     "4 pairs of electrons"),

    ("An octet refers to:",
     ["four single electrons",
      "four pairs of electrons",
      "eight pairs of electrons"],
     "four pairs of electrons"),

    ("Valence electrons are electrons:",
     ["in the nucleus",
      "in the outermost shell of an atom",
      "in the innermost shell"],
     "in the outermost shell of an atom"),

    ("Valence electrons are important because only they:",
     ["determine atomic mass",
      "take part in bonding and chemical reactions",
      "determine nuclear stability"],
     "take part in bonding and chemical reactions"),

    ("How many valence electrons does calcium have?",
     ["four", "two", "six"],
     "two"),

    ("How many valence electrons does bromine have?",
     ["7", "5", "3"],
     "7"),

    ("The Lewis symbol for carbon shows:",
     ["two pairs of electrons",
      "four lone electrons and zero pairs of electrons",
      "one pair and two lone electrons"],
     "four lone electrons and zero pairs of electrons"),

    ("Core electrons reside:",
     ["in the bonding region",
      "below the valence shell",
      "in the outermost shell"],
     "below the valence shell"),

    ("Sodium has atomic number 11. It has ____ core electrons, and ___ valence electrons.",
     ["ten, one", "two, nine", "eight, three"],
     "ten, one"),

    ("The barium ion:",
     ["has a charge of +1 and one valence electron",
      "has a charge of +2, and zero valence electrons",
      "has a charge of -2 and eight valence electrons"],
     "has a charge of +2, and zero valence electrons"),

    ("The aluminum ion:",
     ["has a +1 charge and one valence electron",
      "has a +3 charge and no valence electrons",
      "has a -3 charge and eight valence electrons"],
     "has a +3 charge and no valence electrons"),

    ("The oxide ion:",
     ["has a -1 charge and seven valence electrons",
      "has a -2 charge and eight valence electrons",
      "has a +2 charge and zero valence electrons"],
     "has a -2 charge and eight valence electrons"),

    ("The phosphide ion has:",
     ["a -3 charge and eight valence electrons",
      "a -1 charge and six valence electrons",
      "a +3 charge and zero valence electrons"],
     "a -3 charge and eight valence electrons"),

    ("The cesium ion has:",
     ["one valence electron and a +1 charge",
      "zero valence electrons and a +1 charge",
      "eight valence electrons and a -1 charge"],
     "one valence electron and a +1 charge"),

    ("For main group elements the number of valence electrons:",
     ["is always eight",
      "is equal to the group number",
      "is equal to the period number"],
     "is equal to the group number"),

    ("All group 5A elements have:",
     ["3 valence electrons", "5 valence electrons", "7 valence electrons"],
     "5 valence electrons"),

    ("In the Lewis symbol of an atom:",
     ["only the single electrons form bonds",
      "only paired electrons form bonds",
      "all electrons form bonds"],
     "only the single electrons form bonds"),

    ("Groups 1A, 2A, and 3A elements form ions with these charges:",
     ["+2, +4, +6", "+1, +2, +3", "-1, -2, -3"],
     "+1, +2, +3"),

    ("Elements in groups 1A, 2A and 3A form:",
     ["ionic bonds", "metallic bonds", "covalent bonds"],
     "ionic bonds"),

    ("Elements in group 8A:",
     ["form ionic bonds", "do not form bonds", "form covalent bonds"],
     "do not form bonds"),

    ("In chemical reactions, elements gain or lose electrons to achieve an:",
     ["isotope", "octet", "excited state"],
     "octet"),

    ("Elements in groups 4A to 7A:",
     ["gain electrons to achieve an octet",
      "lose electrons to achieve an octet",
      "share electrons only"],
     "gain electrons to achieve an octet"),

    ("The term 'oxidation state' refers to:",
     ["the number of electron pairs",
      "the charge on an ion of an element",
      "the number of neutrons"],
     "the charge on an ion of an element"),
]

# ---------------------------------------------------------
# USER ANSWERS
# ---------------------------------------------------------
st.subheader("Questions")

user_answers = []
for i, (q, options, correct) in enumerate(questions):
    st.write(f"**{i+1}. {q}**")
    choice = st.radio(
        label="",
        options=options,
        key=f"q{i}",
        index=None
    )
    user_answers.append(choice)
    st.write("---")

# ---------------------------------------------------------
# SUBMIT AND SCORE
# ---------------------------------------------------------
if st.button("Submit Quiz"):
    score = 0
    st.subheader("Results")

    for i, (q, options, correct) in enumerate(questions):
        user_answer = user_answers[i]
        if user_answer == correct:
            score += 1
            st.write(f"**Question {i+1}: Correct!**")
        else:
            st.write(f"**Question {i+1}: Incorrect.** The correct answer is: **{correct}**")

    st.write("---")
    st.write(f"### Your final score: **{score} / {len(questions)}**")

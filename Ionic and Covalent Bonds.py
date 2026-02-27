import streamlit as st

st.set_page_config(page_title="Ionic and Covalent Bonding Quiz")

st.title("Ionic and Covalent Bonding Quiz")
st.write("Select the best answer for each question. No answers are preselected.")

# -----------------------------
# QUIZ DATA
# -----------------------------
questions = [
    ("In a covalent bond, electrons are _____.",
     ["shared between two nonmetals", "free to move throughout a lattice", "transferred from metal to nonmetal"],
     "shared between two nonmetals"),

    ("In an ionic bond, electrons are _____.",
     ["shared equally", "lost by a metal and gained by a nonmetal", "shared between two nonmetals"],
     "lost by a metal and gained by a nonmetal"),

    ("An ionic bond contains: _____.",
     ["two metals", "a cation and an anion", "two nonmetals"],
     "a cation and an anion"),

    ("A covalent bond always contains: _____.",
     ["a metal and a nonmetal", "ions", "atoms"],
     "atoms"),

    ("Another name for a covalent compound is: _____.",
     ["molecular compound", "ionic compound", "metallic compound"],
     "molecular compound"),

    ("What are the two types of covalent bonds?",
     ["cationic and anionic", "ionic and metallic", "nonpolar and polar"],
     "nonpolar and polar"),

    ("In a nonpolar covalent bond, electrons are: _____.",
     ["shared unequally", "shared equally", "transferred completely"],
     "shared equally"),

    ("A bond between hydrogen and fluorine is expected to be: _____.",
     ["nonpolar covalent", "ionic", "polar covalent"],
     "polar covalent"),

    ("A bond between lithium and fluorine is expected to be: _____.",
     ["nonpolar covalent", "ionic", "polar covalent"],
     "ionic"),

    ("The electronegativity values for carbon and fluorine are 2.1 and 4.0. The bond between them is expected to be: _____.",
     ["polar covalent", "nonpolar covalent", "ionic"],
     "polar covalent"),

    ("In a C–F bond, electrons spend more time around: _____.",
     ["both equally", "carbon", "fluorine"],
     "fluorine"),

    ("A bond between two nitrogen atoms is expected to be: _____.",
     ["ionic", "nonpolar covalent", "polar covalent"],
     "nonpolar covalent"),

    ("In the bond between magnesium and oxygen, the magnesium and oxygen have: _____.",
     ["+3 and -3", "+2 and -2", "+1 and -1"],
     "+2 and -2"),

    ("In the bond between aluminum and nitrogen, aluminum ______ while nitrogen ________.",
     ["gains 3 electrons; loses 3 electrons", "loses 3 electrons; gains 3 electrons", "shares 3 electrons; shares 3 electrons"],
     "loses 3 electrons; gains 3 electrons"),

    ("In aluminum nitride, the bond is between an Al cation with a ____ charge and a nitride with a ____ charge.",
     ["+2 and -2", "+3 and -3", "+1 and -1"],
     "+3 and -3"),

    ("In an ammonia (NH₃) molecule, how many nonbonding electron pairs are on nitrogen?",
     ["two", "three", "one"],
     "one"),

    ("The formation of a covalent bond results in: _____.",
     ["formation of ions", "an increase in electron density between the atoms", "electron transfer"],
     "an increase in electron density between the atoms"),

    ("The electrostatic attraction between cation and anion is known as: _____.",
     ["an ionic bond", "a metallic bond", "a covalent bond"],
     "an ionic bond"),

    ("The formation of molecular compounds always involves: _____.",
     ["free-moving electrons", "transfer of electrons", "sharing of electrons"],
     "sharing of electrons"),

    ("In aluminum chloride, how many electrons are gained by a chlorine atom?",
     ["three", "one", "two"],
     "one"),

    ("In a polar covalent bond, electrons are: _____.",
     ["transferred completely", "shared equally", "shared unequally"],
     "shared unequally"),
]

# -----------------------------
# USER ANSWERS
# -----------------------------
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

# -----------------------------
# SUBMIT AND SCORE
# -----------------------------
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

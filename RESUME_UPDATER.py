# filename: resume_updater.py
import os, re

OUTPUT_DIR = r"C:\Users\prasa\OneDrive\Desktop\HASH\RESUME-PROJECT"
OUTPUT_FILE = "updated_resume.txt"


def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def save_text(content):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"\n✅ Updated resume saved at: {out_path}")


def classify_jd_line(line):
    """Classify JD line into resume section."""
    text = line.lower()
    if any(word in text for word in ["python", "java", "c++", "sql", "selenium", "jira",
                                     "framework", "api", "testing", "tools", "javascript",
                                     "node.js", "react", "cloud", "aws", "azure", "gcp"]):
        return "skills"
    elif any(word in text for word in ["responsible", "develop", "implement", "design",
                                       "maintain", "test", "execute", "collaborate", "debug"]):
        return "responsibilities"
    elif any(word in text for word in ["bachelor", "degree", "qualification",
                                       "certification", "graduate"]):
        return "qualifications"
    elif "project" in text or "case study" in text:
        return "projects"
    elif any(word in text for word in ["english", "hindi", "french", "german",
                                       "spanish", "tamil", "telugu"]):
        return "languages"
    else:
        return None


def extract_sections(jd_text):
    """Extract JD into categories by classifying each line."""
    jd_sections = {"skills": [], "responsibilities": [], "qualifications": [], "projects": [], "languages": []}

    for line in jd_text.splitlines():
        clean = line.strip(" -•\t")
        if not clean:
            continue
        section = classify_jd_line(clean)
        if section:
            jd_sections[section].append(clean)

    # Deduplicate + clean
    for k in jd_sections:
        jd_sections[k] = list(set(jd_sections[k]))

    return jd_sections


def boost_summary(resume, jd_sections):
    """Update or insert summary with JD skills."""
    all_skills = [s for s in jd_sections["skills"] if len(s.split()) <= 4]  # keep it short
    if all_skills:
        skill_text = ", ".join(all_skills[:5])
    else:
        skill_text = "software development and problem solving"

    summary = f"Summary\nResults-oriented candidate aligned to this role. Experienced in {skill_text}.\n\n"

    if re.search(r"(career objective|summary)", resume, flags=re.I):
        resume = re.sub(r"(?:^|\n)(career objective|summary).*?(?:\n{2,}|\Z)",
                        summary, resume, flags=re.I | re.S)
    else:
        resume = summary + resume
    return resume


def merge_into_section(resume, section_name, new_items):
    """Insert JD items into the right section only."""
    if not new_items:
        return resume

    # clean bullet points
    clean_items = []
    for item in new_items:
        item = re.sub(r"^(?:-|\d+\.|\•)\s*", "", item)  # strip leading bullet/number
        if len(item.split()) > 15:  # skip long sentences from JD
            continue
        clean_items.append(item)

    if not clean_items:
        return resume

    m = re.search(rf"(?:^|\n)({section_name})\s*\n(.*?)(?:\n{{2,}}|\Z)",
                  resume, flags=re.I | re.S)
    if m:
        full = m.group(0)
        body = m.group(2).strip()
        existing = [line.strip(" -•\t") for line in body.splitlines()]
        missing = [i for i in clean_items if not any(i.lower() in e.lower() for e in existing)]

        if missing:
            new_body = body + "\n" + "\n".join(f"- {m}" for m in missing)
            new = m.group(1).title() + "\n" + new_body + "\n\n"
            return resume.replace(full, new)
    else:
        block = f"\n{section_name.title()}\n" + "\n".join(f"- {i}" for i in clean_items) + "\n\n"
        return resume + block

    return resume


def enhance_projects(resume, jd_sections):
    """Add project descriptions if missing."""
    proj_match = re.search(r"(Projects\s*\n)(.*?)(?:\n{2,}|\Z)",
                           resume, flags=re.I | re.S)
    if not proj_match:
        return resume

    proj_block = proj_match.group(2)
    if "•" not in proj_block and "-" not in proj_block:  # no descriptions
        techs = ", ".join(jd_sections["skills"][:3]) if jd_sections["skills"] else "relevant technologies"
        proj_block += f"\n   • Designed and implemented using {techs}."
        resume = resume.replace(proj_match.group(0),
                                proj_match.group(1) + proj_block + "\n\n")

    return resume


def enforce_structure(resume, jd_sections):
    """Ensure sections are ordered and filled."""
    ordered_sections = ["Summary", "Technical Skills", "Experience", "Projects", "Education", "Languages"]

    # Separate personal info
    personal_info = ""
    first_section_match = re.search(r"(Summary|Technical Skills|Experience|Projects|Education|Languages)",
                                    resume, flags=re.I)
    if first_section_match:
        idx = first_section_match.start()
        personal_info = resume[:idx].strip()
        resume = resume[idx:]
    else:
        personal_info = resume
        resume = ""

    # Map JD parts to resume sections
    section_map = {
        "Technical Skills": jd_sections["skills"],
        "Experience": jd_sections["responsibilities"],
        "Projects": jd_sections["projects"],
        "Education": jd_sections["qualifications"],
        "Languages": jd_sections["languages"],
    }

    for sec, items in section_map.items():
        resume = merge_into_section(resume, sec, items)

    resume = enhance_projects(resume, jd_sections)

    if not re.search(r"(?:^|\n)Summary", resume, flags=re.I):
        resume = boost_summary(resume, jd_sections)

    # Reorder neatly
    section_blocks = {}
    for sec in ordered_sections:
        match = re.search(rf"(?:^|\n)({sec})\s*\n(.*?)(?:\n{{2,}}|\Z)",
                          resume, flags=re.I | re.S)
        if match:
            section_blocks[sec] = match.group(0).strip()

    final_resume = ""
    if personal_info:
        final_resume += personal_info + "\n\n"
    for sec in ordered_sections:
        if sec in section_blocks:
            final_resume += section_blocks[sec] + "\n\n"

    return final_resume.strip()


def update_resume(resume_text, jd_text):
    jd_sections = extract_sections(jd_text)
    out = resume_text
    out = boost_summary(out, jd_sections)
    out = enforce_structure(out, jd_sections)
    return out


def main():
    resume_path = input("Enter full path of your resume .txt file: ").strip()
    resume_text = load_text(resume_path)

    print("\n📌 Paste the Job Description below. End with an empty line:")
    jd_lines = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                break
            jd_lines.append(line)
        except EOFError:
            break
    jd_text = "\n".join(jd_lines)
    if not jd_text.strip():
        print("❌ No Job Description provided. Exiting.")
        return
    updated_resume = update_resume(resume_text, jd_text)
    save_text(updated_resume)


if __name__ == "__main__":
    main()

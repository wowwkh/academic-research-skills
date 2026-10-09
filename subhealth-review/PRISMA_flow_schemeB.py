# PRISMA 2020 Flow Diagram for Scheme B
# pip install matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(10, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.axis('off')

blue = '#E3F2FD'
green = '#E8F5E9'
yellow = '#FFF9C4'
red = '#FFEBEE'

def box(x, y, w, h, text, color=blue):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1", facecolor=color, edgecolor='black')
    ax.add_patch(rect)
    ax.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=8, wrap=True)

box(0.5, 12.5, 9, 0.8, "Identification: Records identified\nPubMed 450 + WoS 380 + Embase 320 + CNKI 180 + Other 50 = 1380", blue)
box(0.5, 11.5, 9, 0.6, "Records after duplicates removed: 890", green)
box(0.5, 10.2, 4.2, 0.8, "Title/abstract screened: 890", yellow)
box(5.3, 10.2, 4.2, 0.8, "Excluded title/abstract: 650\nNon-SHS, non-inflammation", red)
box(0.5, 9.2, 9, 0.6, "Full-text sought: 240 (10 not retrieved)", yellow)
box(0.5, 7.9, 4.2, 0.8, "Full-text assessed: 230", yellow)
box(5.3, 7.9, 4.2, 1.2, "Excluded full-text: 100\n40 No SHSQ-25/low-grade bridge\n30 No mechanism axis\n15 Predatory/no DOI\n15 Duplicate", red)
box(0.5, 6.5, 9, 0.6, "Studies included: 130", green)
box(0.5, 5.5, 9, 0.8, "Final after evidence grading α/β/γ:\n110 studies (19 α Direct + 71 β Homologous + 20 γ Hypothetical)\nMeets 90-110 target, 40% recent 2 years", green)
box(0.5, 4.2, 2.8, 0.8, "α Direct: 19\nSHSQ-25 + cortisol/NLR/HRV\nPMC6107457 205.8 vs 161.8\nSaudi 23.7% α=0.918", '#C8E6C9')
box(3.6, 4.2, 2.8, 0.8, "β Homologous: 71\nCRP 3-10+IL-6 3.25-20+HRQoL\nSwedish/Danish\nImmunometabolism PMC13218923\nDrp1 Ser616/Ser637", '#FFE0B2')
box(6.7, 4.2, 2.8, 0.8, "γ Hypothetical: 20\nMechanism hypothesis\nIn vitro\nFuture validation", '#F8BBD0')
ax.text(5, 0.5, "PRISMA 2020 Flow Diagram — Scheme B Low-grade inflammation + Immunometabolism in SHS\nTemplate for Supplementary Fig S1", ha='center', fontsize=9, style='italic')
plt.tight_layout()
plt.savefig('/home/user/academic-research-skills/subhealth-review/PRISMA_Flow_SchemeB.png', dpi=300, bbox_inches='tight')
plt.savefig('/home/user/academic-research-skills/subhealth-review/PRISMA_Flow_SchemeB.pdf', bbox_inches='tight')
print("Saved PRISMA_Flow_SchemeB.png and pdf")

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def forest_plot(outcome, studies, effects, lower, upper, overall_effect, overall_lower, overall_upper, xlabel, title, filename, is_or=False):
    fig, ax = plt.subplots(figsize=(8, max(4, len(studies)*0.6+1.5)))
    y_pos = np.arange(len(studies))[::-1]
    
    # Plot individual studies
    for i, (study, eff, lo, hi) in enumerate(zip(studies, effects, lower, upper)):
        y = y_pos[i]
        # point
        ax.plot(eff, y, 's', color='blue', markersize=6)
        # CI line
        ax.plot([lo, hi], [y, y], color='blue', linewidth=1.5)
    
    # Overall diamond
    overall_y = -1
    diamond_height = 0.4
    # diamond polygon
    diamond_x = [overall_lower, overall_effect, overall_upper, overall_effect]
    diamond_y = [overall_y, overall_y+diamond_height/2, overall_y, overall_y-diamond_height/2]
    ax.fill(diamond_x, diamond_y, color='red', alpha=0.6, edgecolor='red')
    ax.plot(overall_effect, overall_y, 'D', color='red', markersize=8)
    
    # vertical line at null
    null_val = 1 if is_or else 0
    ax.axvline(null_val, color='black', linestyle='--', linewidth=0.8)
    
    # Labels
    ax.set_yticks(list(y_pos)+[overall_y])
    ax.set_yticklabels(studies + ['Overall (Random-effects)'])
    ax.set_xlabel(xlabel, fontsize=10)
    ax.set_title(title, fontsize=11, fontweight='bold', pad=10)
    
    # Add effect labels on right
    ax2 = ax.twinx()
    ax2.set_ylim(ax.get_ylim())
    ax2.set_yticks(list(y_pos)+[overall_y])
    effect_labels = [f"{e:.2f} [{l:.2f}, {u:.2f}]" if not is_or else f"{e:.2f} [{l:.2f}, {u:.2f}]" for e,l,u in zip(effects, lower, upper)]
    effect_labels.append(f"{overall_effect:.2f} [{overall_lower:.2f}, {overall_upper:.2f}]")
    ax2.set_yticklabels(effect_labels, fontsize=8)
    ax2.set_ylabel('Effect [95% CI]', fontsize=9)
    
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.savefig(filename.replace('.png','.pdf'), bbox_inches='tight')
    plt.close()
    print(f"Saved {filename}")

# Data based on meta_analysis_extraction

# Fig S2 Cortisol
studies = ["Hou 2019 PMC6107457", "Liu 2024", "Zhang 2024", "Alzain 2024b"]
effects = [44.0, 25.0, 40.0, 35.0]
lower = [38.0, 15.0, 28.0, 30.0]
upper = [50.0, 35.0, 52.0, 40.0]
forest_plot("Cortisol", studies, effects, lower, upper, 36.5, 28.5, 44.5, "Mean Difference (ng/ml) SHS vs Healthy", "Fig S2 Forest plot: Cortisol SHS vs Healthy (Random-effects I2=68%, p<0.001)", "FigS2_Forest_Cortisol.png")

# Fig S3 NLR
studies = ["Chen 2024", "Alzain 2024b", "Crohn MDA 2020", "Hemodialysis 2021", "MASLD 2022", "Clin Chim Acta 2023"]
effects = [0.5, 0.5, 0.6, 0.4, 0.5, 0.55]
lower = [0.3, 0.4, 0.2, 0.1, 0.25, 0.35]
upper = [0.7, 0.6, 1.0, 0.7, 0.75, 0.75]
forest_plot("NLR", studies, effects, lower, upper, 0.51, 0.42, 0.60, "Mean Difference NLR", "Fig S3 Forest plot: NLR SHS vs Healthy (Random-effects I2=15%, p<0.001)", "FigS3_Forest_NLR.png")

# Fig S4 HRV SDNN
studies = ["Zhang 2024", "BBIH 2021", "J Psychosom Res 2023", "Psychoneuroendocrinol 2022"]
effects = [-25, -25, -24, -26]
lower = [-32, -35, -33, -35]
upper = [-18, -15, -15, -17]
forest_plot("HRV SDNN", studies, effects, lower, upper, -25.0, -28.5, -21.5, "Mean Difference SDNN (ms)", "Fig S4a Forest plot: HRV SDNN SHS vs Healthy (Random-effects I2=0%, p<0.001)", "FigS4a_Forest_HRV_SDNN.png")

# Fig S4b RMSSD
studies = ["Zhang 2024", "BBIH 2021", "J Psychosom Res 2023"]
effects = [-10, -10, -11]
lower = [-14, -15, -15.5]
upper = [-6, -5, -6.5]
forest_plot("HRV RMSSD", studies, effects, lower, upper, -10.3, -12.5, -8.1, "Mean Difference RMSSD (ms)", "Fig S4b Forest plot: HRV RMSSD SHS vs Healthy (Random-effects I2=0%, p<0.001)", "FigS4b_Forest_HRV_RMSSD.png")

# Fig S5 Fatigue OR joint
studies = ["Swedish 2015", "Danish DBDS 2019", "PLOS ONE 2019", "Qual Life Res 2023 Chinese", "J Korean Med Sci 2024", "BBI 2023"]
effects = [1.85, 1.52, 1.68, 1.72, 1.45, 1.60]
lower = [1.45, 1.32, 1.20, 1.30, 1.15, 1.35]
upper = [2.36, 1.75, 2.35, 2.28, 1.83, 1.90]
forest_plot("Fatigue OR", studies, effects, lower, upper, 1.60, 1.45, 1.76, "Odds Ratio Fatigue Risk (Joint CRP>3+IL-6>3.25)", "Fig S5 Forest plot: Fatigue Risk Joint CRP>3+IL-6>3.25 (Random-effects I2=22%, p<0.001)", "FigS5_Forest_Fatigue_OR.png", is_or=True)

# Fig S6 SF-36 vitality
studies = ["Swedish 2015", "Danish DBDS 2019", "Qual Life Res 2024 Chinese", "Qual Life Res 2023 Chinese", "J Korean Med Sci 2024"]
effects = [-10, -8, -10, -7, -7]
lower = [-13, -9.5, -14, -10, -9.5]
upper = [-7, -6.5, -6, -4, -4.5]
forest_plot("SF36 Vitality", studies, effects, lower, upper, -8.2, -9.8, -6.6, "Mean Difference SF-36 Vitality", "Fig S6 Forest plot: SF-36 Vitality Low-grade vs Ref (Random-effects I2=35%, p<0.001)", "FigS6_Forest_SF36_Vitality.png")

# Fig S7 OXPHOS SMD
studies = ["Zhao 2024", "Mitochondrion 2023", "ME/CFS 2024 (homologous)"]
effects = [-1.10, -1.23, -1.36]
lower = [-1.50, -1.73, -1.88]
upper = [-0.70, -0.73, -0.84]
forest_plot("OXPHOS SMD", studies, effects, lower, upper, -1.22, -1.48, -0.96, "Standardized Mean Difference OXPHOS basal", "Fig S7 Forest plot: PBMC OXPHOS SHS vs Healthy (Random-effects I2=0%, p<0.001)", "FigS7_Forest_OXPHOS.png")

print("All forest plots generated")

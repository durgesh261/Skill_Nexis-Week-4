import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import numpy as np

def generate_powerbi_preview():
    visuals_dir = os.path.join(os.path.dirname(__file__), "..", "visuals")
    os.makedirs(visuals_dir, exist_ok=True)
    out_path = os.path.join(visuals_dir, "powerbi_dashboard_preview.png")

    fig = plt.figure(figsize=(15, 9), facecolor='#0F172A')
    gs = gridspec.GridSpec(3, 4, figure=fig, height_ratios=[0.55, 1.2, 1.2], hspace=0.35, wspace=0.25)

    # Title & Banner
    ax_title = fig.add_subplot(gs[0, :])
    ax_title.set_facecolor('#1E293B')
    ax_title.axis('off')
    
    # Yellow Power BI bar on left
    ax_title.add_patch(plt.Rectangle((0, 0), 0.015, 1, color='#F2C811', transform=ax_title.transAxes))
    
    # Title text
    ax_title.text(0.03, 0.65, "GLOBAL COMMERCIAL & FINANCIAL PERFORMANCE DASHBOARD", 
                  color='#F8FAFC', fontsize=16, fontweight='bold', transform=ax_title.transAxes)
    ax_title.text(0.03, 0.30, "Power BI Capstone Project | Microsoft Financial Sample Dataset (700 Transactions | 2013-2014)", 
                  color='#94A3B8', fontsize=11, transform=ax_title.transAxes)

    # KPI 1: Net Sales
    ax_title.text(0.60, 0.70, "NET SALES REVENUE", color='#94A3B8', fontsize=9, fontweight='bold', transform=ax_title.transAxes)
    ax_title.text(0.60, 0.25, "$118.73M", color='#38BDF8', fontsize=16, fontweight='bold', transform=ax_title.transAxes)

    # KPI 2: Net Profit
    ax_title.text(0.73, 0.70, "NET OPERATING PROFIT", color='#94A3B8', fontsize=9, fontweight='bold', transform=ax_title.transAxes)
    ax_title.text(0.73, 0.25, "$16.89M", color='#10B981', fontsize=16, fontweight='bold', transform=ax_title.transAxes)

    # KPI 3: Margin
    ax_title.text(0.88, 0.70, "PROFIT MARGIN", color='#94A3B8', fontsize=9, fontweight='bold', transform=ax_title.transAxes)
    ax_title.text(0.88, 0.25, "14.23%", color='#F59E0B', fontsize=16, fontweight='bold', transform=ax_title.transAxes)

    # Visual 1: Country Sales & Profit
    ax1 = fig.add_subplot(gs[1, 0:2])
    ax1.set_facecolor('#1E293B')
    countries = ['USA', 'Canada', 'France', 'Germany', 'Mexico']
    sales = [25.03, 24.89, 24.31, 23.51, 20.99]
    profit = [2.99, 3.53, 3.78, 3.68, 2.91]
    x = np.arange(len(countries))
    w = 0.35
    ax1.bar(x - w/2, sales, w, label='Sales ($M)', color='#0284C7', edgecolor='none')
    ax1.bar(x + w/2, profit, w, label='Profit ($M)', color='#10B981', edgecolor='none')
    ax1.set_title('Sales & Profit by Country ($M USD)', color='#F8FAFC', fontsize=11, fontweight='bold', pad=10)
    ax1.set_xticks(x)
    ax1.set_xticklabels(countries, color='#94A3B8', fontsize=9)
    ax1.tick_params(colors='#94A3B8')
    ax1.legend(facecolor='#1E293B', edgecolor='#334155', labelcolor='#F8FAFC', fontsize=8)
    ax1.grid(color='#334155', linestyle='--', alpha=0.5, axis='y')

    # Visual 2: Segment Donut
    ax2 = fig.add_subplot(gs[1, 2:4])
    ax2.set_facecolor('#1E293B')
    segments = ['Government\n(44.2%)', 'Small Business\n(35.7%)', 'Enterprise\n(16.5%)', 'Midmarket\n(2.0%)', 'Channel Partners\n(1.5%)']
    seg_sales = [52.51, 42.42, 19.65, 2.38, 1.77]
    colors = ['#38BDF8', '#10B981', '#F59E0B', '#C084FC', '#FB7185']
    wedges, texts = ax2.pie(seg_sales, labels=segments, colors=colors, startangle=140,
                            wedgeprops=dict(width=0.45, edgecolor='#1E293B', linewidth=2),
                            textprops=dict(color='#F8FAFC', fontsize=8))
    ax2.set_title('Revenue Mix by Customer Segment', color='#F8FAFC', fontsize=11, fontweight='bold', pad=10)

    # Visual 3: Product Profitability
    ax3 = fig.add_subplot(gs[2, 0:2])
    ax3.set_facecolor('#1E293B')
    products = ['Paseo', 'VTT', 'Amarilla', 'Carretera', 'Montana', 'Velo']
    prod_sales = [33.01, 20.51, 19.04, 15.62, 15.39, 15.17]
    prod_profit = [4.80, 3.03, 2.81, 2.12, 2.11, 2.02]
    xp = np.arange(len(products))
    ax3.bar(xp - w/2, prod_sales, w, label='Sales ($M)', color='#38BDF8')
    ax3.bar(xp + w/2, prod_profit, w, label='Profit ($M)', color='#F59E0B')
    ax3.set_title('Product Line Revenue vs. Net Profit ($M)', color='#F8FAFC', fontsize=11, fontweight='bold', pad=10)
    ax3.set_xticks(xp)
    ax3.set_xticklabels(products, color='#94A3B8', fontsize=9)
    ax3.tick_params(colors='#94A3B8')
    ax3.legend(facecolor='#1E293B', edgecolor='#334155', labelcolor='#F8FAFC', fontsize=8)
    ax3.grid(color='#334155', linestyle='--', alpha=0.5, axis='y')

    # Visual 4: Monthly Trend Line
    ax4 = fig.add_subplot(gs[2, 2:4])
    ax4.set_facecolor('#1E293B')
    months = ['Sep 13', 'Nov 13', 'Jan 14', 'Mar 14', 'May 14', 'Jul 14', 'Sep 14', 'Nov 14', 'Dec 14']
    trend_sales = [5.2, 6.9, 4.3, 6.4, 6.8, 5.9, 8.9, 11.2, 13.0]
    ax4.plot(months, trend_sales, marker='o', color='#38BDF8', linewidth=2.5, markersize=5)
    ax4.fill_between(months, trend_sales, color='#38BDF8', alpha=0.15)
    ax4.set_title('Historical Monthly Revenue Growth ($M USD)', color='#F8FAFC', fontsize=11, fontweight='bold', pad=10)
    ax4.tick_params(colors='#94A3B8')
    ax4.grid(color='#334155', linestyle='--', alpha=0.5, axis='y')

    plt.tight_layout()
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"Power BI dashboard preview saved to: {out_path}")

if __name__ == "__main__":
    generate_powerbi_preview()

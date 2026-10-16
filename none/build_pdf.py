#!/usr/bin/env python3
"""Build A4 Chinese PDF from SKHY strategy report image (per pdf_rule)."""

from pathlib import Path

from weasyprint import HTML

ROOT = Path("/workspace")
NONE = ROOT / "none"
PRODUCTS = ROOT / "products"
QR_PATH = NONE / "qr.png"
OUT_PDF = PRODUCTS / "RUIDU_SKHY_超短期投资策略报告_20261016.pdf"

HTML_DOC = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<style>
  @page {{
    size: A4;
    margin: 16mm 18mm;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: "Noto Sans CJK SC", "Noto Sans CJK", "WenQuanYi Micro Hei", sans-serif;
    font-size: 10.5pt;
    line-height: 1.55;
    color: #111;
  }}
  h1 {{
    font-size: 14pt;
    font-weight: 700;
    margin: 6pt 0 8pt;
    line-height: 1.4;
  }}
  h2 {{
    font-size: 12pt;
    font-weight: 700;
    margin: 12pt 0 6pt;
    page-break-after: avoid;
  }}
  h3 {{
    font-size: 11pt;
    font-weight: 700;
    margin: 8pt 0 4pt;
    page-break-after: avoid;
  }}
  p {{ margin: 0 0 6pt; text-align: justify; }}
  ul {{ margin: 0 0 6pt; padding-left: 1.2em; }}
  li {{ margin: 0 0 3pt; }}
  .meta {{
    font-size: 9pt;
    color: #333;
    margin: 0 0 4pt;
  }}
  .divider {{
    border: none;
    border-top: 0.6pt solid #000;
    margin: 6pt 0 10pt;
  }}
  .divider-light {{
    border: none;
    border-top: 0.4pt solid #888;
    margin: 10pt 0 8pt;
  }}
  .section {{
    page-break-inside: avoid;
  }}
  .thesis {{
    page-break-inside: avoid;
  }}
  .final {{
    page-break-inside: avoid;
  }}
  .footer-note {{
    font-size: 8.5pt;
    color: #444;
    line-height: 1.45;
  }}
  .qr {{
    margin-top: 8pt;
    width: 32mm;
    height: 32mm;
  }}
  strong {{ font-weight: 700; }}
</style>
</head>
<body>

<p class="meta">摘录自【长期主义投资认知学习社区】</p>
<h1>RUIDU 定量超短期投资策略报告（机构专供，星球独享，谢绝外传）</h1>
<p class="meta">2026年10月16日｜美国股票｜机构研究专供</p>
<h1>SKHY：从传统周期性存储芯片制造商，转型为核心 AI 超增长资产！</h1>
<hr class="divider"/>

<div class="section">
<h2>一、最新市场表现与投资机会</h2>
<ul>
  <li>10月15日收盘价：$146.11，下跌 0.98%</li>
  <li>近期高点：10月5日 $195.02</li>
  <li>自近期高点回撤：25.1%</li>
  <li>盘中低点：$137.80</li>
</ul>
<p>急剧回调已使 SKHY 进入潜在的战略性建仓区间。然而，在启动建仓之前，必须确认价格企稳以及机构买入支撑。</p>
</div>

<h2>二、五大核心投资论点</h2>

<div class="thesis">
<h3>1. 盈利爆发式增长</h3>
<p>2026年第二季度，营收同比增长 257%，营业利润增长 557%，营业利润率高达 76%。</p>
<p>这些数据表明盈利能力大幅改善；不过，净利润中的部分构成包含非经常性收益。</p>
</div>

<div class="thesis">
<h3>2. AI 超级智能投资浪潮</h3>
<p>美国主导的 AI 超级智能竞赛不断加速，正在推动对算力基础设施前所未有的需求。</p>
<p>随着 GPU 算力扩张，高带宽内存（HBM）需求预计将显著上升。</p>
<p>SK 海力士在这一高性能 AI 存储供应链中占据战略关键位置。</p>
</div>

<div class="thesis">
<h3>3. 与英伟达的深度战略合作</h3>
<p>SK 海力士与英伟达正推进下一代 HBM 技术的联合研发，并加强长期供应合作。</p>
<p>这一战略关系增强了 SK 海力士的技术竞争优势、客户关系以及未来订单可见度。</p>
</div>

<div class="thesis">
<h3>4. 结构性增长与估值重估</h3>
<p>HBM4 的商业化与放量交付，标志着高端存储技术迈出重要一步。</p>
<p>随着 AI 驱动的存储需求日益成为盈利贡献的重要来源，SK 海力士有望从传统周期性半导体估值框架，转向反映其作为 AI 增长龙头地位的估值体系。</p>
</div>

<div class="thesis">
<h3>5. 潜在的超跌交易机会</h3>
<p>自近期高点回撤 25.1% 后，SKHY 已进入技术上具有重要意义的观察区间。</p>
<p>然而，单纯的急剧下跌并不构成买入机会。</p>
<p>RUIDU 要求在确认资金重新流入、机构建仓以及技术面企稳之后，才会执行交易。</p>
</div>

<div class="section">
<h2>三、关键风险提示</h2>
<h3>显著的 ADR 溢价风险</h3>
<p>SKHY 在美国交易的股份，相对于公司在韩国上市的正股，似乎存在显著的估值溢价。</p>
<p>第三方估计显示，ADR 溢价约为 51.9%，仍有待独立核实。</p>
<p>即便 SK 海力士持续交付出色的盈利增长，该溢价的收敛仍可能对美国交易股份形成显著下行压力，且独立于公司基本面表现。</p>
<p>其他风险还包括：</p>
<ul>
  <li>全球 HBM 市场竞争加剧</li>
  <li>AI 基础设施资本开支放缓</li>
  <li>半导体存储周期反转</li>
  <li>盈利与估值可能压缩</li>
</ul>
<p>强劲的公司基本面并不能消除股权估值风险。</p>
</div>

<div class="section">
<h2>四、RUIDU 超短期交易策略</h2>
<h3>方案 A｜优先战略建仓</h3>
<ul>
  <li>入场区间：$135–$140</li>
  <li>组合最大仓位：15%</li>
</ul>
<h3>方案 B｜企稳后的备选入场</h3>
<ul>
  <li>入场区间：$137–$145</li>
  <li>组合最大仓位：10%</li>
</ul>
<h3>执行与风险管理规则</h3>
<p>方案 A 与方案 B 为互斥备选，其仓位配置不得叠加。</p>
<ul>
  <li>强制最大止损：低于实际平均入场成本 20%</li>
  <li>若技术趋势或原投资论点被证伪，应更早离场。</li>
  <li>绝不使用杠杆。</li>
  <li>绝不追高。</li>
  <li>绝不盲目摊薄成本。</li>
</ul>
<p>资本保全与纪律性执行优先于收益最大化。</p>
</div>

<div class="section">
<h2>五、一至三个月情景分析</h2>
<p>情景｜参考价格区间</p>
<ul>
  <li>看涨修复：$160–$175</li>
  <li>震荡整理／基准情形：$135–$160</li>
  <li>继续下行风险：低于 $135</li>
</ul>
<p>上述区间为条件性交易情景，而非保证性价格目标。</p>
<p>实际结果将取决于盈利表现、AI 板块资金流向、估值动态以及更广泛的市场环境。</p>
</div>

<div class="final">
<h2>六、最终投资结论</h2>
<p>SK 海力士的长期投资机会，植根于全球 AI 超级智能建设加速、HBM 需求的结构性增长，以及盈利与估值持续重估的潜力。</p>
<p>其短期交易机会，则在于急剧回调之后，机构资金重新流入与估值修复的可能。</p>
<p>伟大的行业并不总是意味着伟大的股价。</p>
<p>伟大的公司并不总是意味着绝佳的入场点。</p>
<p>RUIDU 的投资理念始终不变：</p>
<ul>
  <li>基于基本面选股。</li>
  <li>通过定量信号确认入场点。</li>
  <li>以严格仓位限制管理敞口。</li>
  <li>基于纪律性的风险收益分析执行交易。</li>
</ul>
<p>目标并非预测每一次市场波动，而是识别潜在收益足以覆盖风险的非对称机会。</p>
<p><strong>RUIDU 定量投资研究</strong></p>
<p>2026年10月16日</p>
<p class="footer-note"><strong>风险披露：</strong>本报告为基于所提供材料的浓缩研究摘要。财务数据、ADR 溢价估计及市场价格未经独立核实。所有入场水平、情景区间与风险参数仅供研究与说明之用，不构成保证收益或个性化投资建议。投资股票涉及重大风险，包括可能损失本金。</p>
<p>作者：Cedar</p>
<hr class="divider-light"/>
<p class="meta">知识星球｜微信扫码查看原文</p>
<img class="qr" src="{QR_PATH.as_uri()}" alt="知识星球二维码"/>
</div>

</body>
</html>
"""


def build() -> None:
    PRODUCTS.mkdir(parents=True, exist_ok=True)
    NONE.mkdir(parents=True, exist_ok=True)
    html_path = NONE / "report.html"
    html_path.write_text(HTML_DOC, encoding="utf-8")
    HTML(filename=str(html_path), base_url=str(NONE)).write_pdf(str(OUT_PDF))
    print(f"Wrote {OUT_PDF}")


if __name__ == "__main__":
    build()

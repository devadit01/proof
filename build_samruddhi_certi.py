"""
build_samruddhi_certi.py
Builds samruddhi_paper_data.json and generates the publication proof HTML
for Samruddhi Nilesh Deshmukh's JBSAC publication proof.
"""

import json
import os
import sys
from pathlib import Path

# Add skill path for generate_paper_certi
SKILL_DIR = Path(r"C:\Users\Luci M\.gemini\config\skills\paper-certi")
sys.path.append(str(SKILL_DIR))
from generate_paper_certi import generate_html, load_template

# 1. First Page Table Preview HTML
first_page_table_html = """<h4>
                  <span>&#128300;</span>
                  <span>Table 1: Master Formulation Composition &amp; Batch Optimization Matrix (100g Batch)</span>
                </h4>
                <div class="table-view-toggle">
                  <button type="button" class="tbl-toggle-btn active" id="btn-view-f3" onclick="setBatchView('f3')">
                    <span>&#9733;</span> Optimized Batch F3
                  </button>
                  <button type="button" class="tbl-toggle-btn" id="btn-view-all" onclick="setBatchView('all')">
                    <span>&#8644;</span> Compare All Batches
                  </button>
                </div>
                <div class="table-scroll-hint" id="table-scroll-hint-bar" style="display:none;">&#8644; Scroll horizontally to inspect batch formulas &rarr;</div>
                <div class="table-container view-f3" id="formulation-table-container">
                  <table>
                    <thead>
                      <tr>
                        <th class="col-sticky col-ingredient">Ingredient / Role</th>
                        <th class="col-target">Target<br><span class="col-sub">% w/w</span></th>
                        <th class="col-f1">Batch F1<br><span class="col-sub">0.30% Carb.</span></th>
                        <th class="col-f2">Batch F2<br><span class="col-sub">0.50% Carb.</span></th>
                        <th class="col-f3">Batch F3 &starf;<br><span class="col-sub">0.40% (Opt.)</span></th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td class="col-sticky col-ingredient"><strong>Salicylic Acid</strong> (Keratolytic Active)</td>
                        <td class="col-target">2.00%</td>
                        <td class="col-f1">2.00 g</td>
                        <td class="col-f2">2.00 g</td>
                        <td class="col-f3"><strong>2.00 g</strong></td>
                      </tr>
                      <tr>
                        <td class="col-sticky col-ingredient"><strong>Turmeric Extract</strong> (Botanical Active)</td>
                        <td class="col-target">10.00%</td>
                        <td class="col-f1">10.00 g</td>
                        <td class="col-f2">10.00 g</td>
                        <td class="col-f3"><strong>10.00 g</strong></td>
                      </tr>
                      <tr>
                        <td class="col-sticky col-ingredient"><strong>Propylene Glycol</strong> (Co-solvent)</td>
                        <td class="col-target">15.00%</td>
                        <td class="col-f1">15.00 g</td>
                        <td class="col-f2">15.00 g</td>
                        <td class="col-f3"><strong>15.00 g</strong></td>
                      </tr>
                      <tr>
                        <td class="col-sticky col-ingredient"><strong>Glycerine</strong> (Skin Humectant)</td>
                        <td class="col-target">3.00%</td>
                        <td class="col-f1">3.00 g</td>
                        <td class="col-f2">3.00 g</td>
                        <td class="col-f3"><strong>3.00 g</strong></td>
                      </tr>
                      <tr>
                        <td class="col-sticky col-ingredient"><strong>Sorbitol</strong> (Plasticizer)</td>
                        <td class="col-target">1.00%</td>
                        <td class="col-f1">1.00 g</td>
                        <td class="col-f2">1.00 g</td>
                        <td class="col-f3"><strong>1.00 g</strong></td>
                      </tr>
                      <tr>
                        <td class="col-sticky col-ingredient"><strong>Methyl Propylene Glycol</strong> (Enhancer)</td>
                        <td class="col-target">1.00%</td>
                        <td class="col-f1">1.00 g</td>
                        <td class="col-f2">1.00 g</td>
                        <td class="col-f3"><strong>1.00 g</strong></td>
                      </tr>
                      <tr>
                        <td class="col-sticky col-ingredient"><strong>Carbopol 940</strong> (Polymer Matrix)</td>
                        <td class="col-target">0.40%</td>
                        <td class="col-f1">0.30 g</td>
                        <td class="col-f2">0.50 g</td>
                        <td class="col-f3"><strong>0.40 g</strong></td>
                      </tr>
                      <tr>
                        <td class="col-sticky col-ingredient"><strong>Triethanolamine (TEA)</strong> (Buffer)</td>
                        <td class="col-target">pH 5.8</td>
                        <td class="col-f1">3 drops</td>
                        <td class="col-f2">8 drops</td>
                        <td class="col-f3"><strong>q.s. (pH 5.8)</strong></td>
                      </tr>
                      <tr>
                        <td class="col-sticky col-ingredient"><strong>Purified Water</strong> (Vehicle)</td>
                        <td class="col-target">q.s. 100%</td>
                        <td class="col-f1">q.s. 100 g</td>
                        <td class="col-f2">q.s. 100 g</td>
                        <td class="col-f3"><strong>q.s. 100 g</strong></td>
                      </tr>
                    </tbody>
                  </table>
                </div>"""

# 2. Tab 2 Cards Grid HTML (Comparing Batches F1, F2, F3)
tab2_cards_grid_html = """<!-- Batch F1 -->
          <div class="batch-card">
            <div class="batch-code">Batch F1</div>
            <div class="batch-sles">0.30% Carbopol 940 &bull; 3 Drops TEA</div>
            <div class="batch-metrics">
              <div class="metric-item">
                <span class="name">Viscosity (cP)</span>
                <span class="val">8,200 &plusmn; 210</span>
              </div>
              <div class="metric-item">
                <span class="name">Spreadability</span>
                <span class="val">28.50 g&middot;cm/s</span>
              </div>
              <div class="metric-item">
                <span class="name">pH Value</span>
                <span class="val">4.90 &plusmn; 0.10</span>
              </div>
              <div class="metric-item">
                <span class="name">Centrifugation (3k rpm)</span>
                <span class="val">Slight Bleed</span>
              </div>
            </div>
            <div class="batch-desc-note">
              <strong>Evaluation:</strong> Under-crosslinked polymeric matrix with inadequate structural yield. Fluid consistency causes excessive runnability and poor localized residence time upon skin application.
            </div>
          </div>

          <!-- Batch F2 -->
          <div class="batch-card">
            <div class="batch-code">Batch F2</div>
            <div class="batch-sles">0.50% Carbopol 940 &bull; 8 Drops TEA</div>
            <div class="batch-metrics">
              <div class="metric-item">
                <span class="name">Viscosity (cP)</span>
                <span class="val">38,500 &plusmn; 650</span>
              </div>
              <div class="metric-item">
                <span class="name">Spreadability</span>
                <span class="val">11.20 g&middot;cm/s</span>
              </div>
              <div class="metric-item">
                <span class="name">pH Value</span>
                <span class="val">7.40 &plusmn; 0.15</span>
              </div>
              <div class="metric-item">
                <span class="name">Centrifugation (3k rpm)</span>
                <span class="val">0% Separation</span>
              </div>
            </div>
            <div class="batch-desc-note">
              <strong>Evaluation:</strong> Over-crosslinked rigid network with rubbery rheology. Elevated alkaline pH compromises Salicylic Acid bioavailability (shifts unionized fraction) and carries potential skin irritation risk.
            </div>
          </div>

          <!-- Batch F3 (Optimized) -->
          <div class="batch-card" style="border: 2px solid var(--gold-primary); background: #fffdf9; box-shadow: 0 4px 16px rgba(201,168,106,0.18);">
            <div style="position: absolute; top: -10px; right: 14px; background: var(--gold-gradient); color: #fff; font-size: 10px; font-weight: 700; padding: 2px 10px; border-radius: 20px; letter-spacing: 0.08em; text-transform: uppercase;">
              &#9733; Optimized Formula
            </div>
            <div class="batch-code">Batch F3</div>
            <div class="batch-sles">0.40% Carbopol 940 &bull; Controlled TEA Buffer</div>
            <div class="batch-metrics">
              <div class="metric-item">
                <span class="name">Viscosity (cP)</span>
                <span class="val" style="color: #b57a2e; font-weight: 700;">21,400 &plusmn; 350</span>
              </div>
              <div class="metric-item">
                <span class="name">Spreadability</span>
                <span class="val">18.75 g&middot;cm/s</span>
              </div>
              <div class="metric-item">
                <span class="name">pH Value</span>
                <span class="val">5.80 &plusmn; 0.15</span>
              </div>
              <div class="metric-item">
                <span class="name">Centrifugation (3k rpm)</span>
                <span class="val" style="color: #059669; font-weight: 600;">0% Separation</span>
              </div>
            </div>
            <div class="batch-desc-note">
              <strong>Optimal Benchmark:</strong> Ideal pseudoplastic shear-thinning flow, effortless topical spread, stable golden-amber clarity, zero crystalline precipitation, and harmonious compatibility with skin's physiological acid mantle.
            </div>
          </div>"""

# 3. Tab 2 Full Table HTML (Full Table 2 from research paper: Physicochemical Evaluation Matrix)
tab2_full_table_html = """<table class="full-data-table">
            <thead>
              <tr>
                <th class="col-sticky">Evaluated Parameter</th>
                <th>Standard Acceptance Criteria</th>
                <th>Test Apparatus / Method</th>
                <th style="background:#fbf3e2; color:#845a16; border-bottom: 2px solid var(--gold-primary);">Optimized Batch F3 &starf;</th>
                <th>Marketed Control (2% BHA Gel)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="col-sticky"><strong>Appearance</strong></td>
                <td>Smooth, homogeneous gel matrix</td>
                <td>Visual inspection under white backdrop</td>
                <td style="background:#fffdf7; font-weight:600;"><span style="color:#059669; font-weight:600;">Translucent, smooth hydrogel</span></td>
                <td>Clear, transparent gel</td>
              </tr>
              <tr>
                <td class="col-sticky"><strong>Clarity</strong></td>
                <td>Semi-transparent to clear; no precipitation</td>
                <td>Direct transmitted light check</td>
                <td style="background:#fffdf7; font-weight:600;">Semi-transparent (rich golden tint)</td>
                <td>Transparent colorless</td>
              </tr>
              <tr>
                <td class="col-sticky"><strong>Odour</strong></td>
                <td>Pleasant characteristic herbal scent; no rancidity</td>
                <td>Olfactory sensory assessment</td>
                <td style="background:#fffdf7; font-weight:600;">Characteristic mild turmeric scent</td>
                <td>Synthetic masking fragrance</td>
              </tr>
              <tr>
                <td class="col-sticky"><strong>Colour</strong></td>
                <td>Uniform botanical hue corresponding to active</td>
                <td>Visual standard chromatic chart</td>
                <td style="background:#fffdf7; font-weight:600;">Golden yellow to warm amber</td>
                <td>Colorless / off-white</td>
              </tr>
              <tr>
                <td class="col-sticky"><strong>Uniformity</strong></td>
                <td>Homogeneous across top, middle, bottom layers</td>
                <td>Multi-strata batch visual sampling</td>
                <td style="background:#fffdf7; font-weight:600;">Highly uniform throughout</td>
                <td>Highly uniform throughout</td>
              </tr>
              <tr>
                <td class="col-sticky"><strong>Particulate Matter</strong></td>
                <td>Free of gritty or undissolved crystalline solids</td>
                <td>Optical light microscopy (10&times; / 40&times;)</td>
                <td style="background:#fffdf7; font-weight:600;">Completely particle-free</td>
                <td>Completely particle-free</td>
              </tr>
              <tr>
                <td class="col-sticky"><strong>Agglomerates / Lumps</strong></td>
                <td>Absence of polymer lumps or aggregates</td>
                <td>Dual glass slide compression smear test</td>
                <td style="background:#fffdf7; font-weight:600;">Zero lump formation observed</td>
                <td>Zero lump formation observed</td>
              </tr>
              <tr>
                <td class="col-sticky"><strong>Phase Separation</strong></td>
                <td>Stable gel integrity; 0% syneresis</td>
                <td>Centrifugation (3,000 rpm &times; 30 min)</td>
                <td style="background:#fffdf7; font-weight:600;"><span style="color:#059669; font-weight:600;">Stable &bull; 0% phase separation</span></td>
                <td>Stable &bull; 0% phase separation</td>
              </tr>
              <tr>
                <td class="col-sticky"><strong>pH Value (25&deg;C)</strong></td>
                <td>Physiological skin compatibility (4.5 &ndash; 6.5)</td>
                <td>Digital calibrated pH electrode meter</td>
                <td style="background:#fffdf7; font-weight:700; color:#1a1816;">5.80 &plusmn; 0.15</td>
                <td>5.50 &plusmn; 0.10</td>
              </tr>
              <tr>
                <td class="col-sticky"><strong>Viscosity (cP)</strong></td>
                <td>Target cosmetic range (15,000 &ndash; 30,000 cP)</td>
                <td>Brookfield Viscometer (Spindle 6, 20 rpm)</td>
                <td style="background:#fffdf7; font-weight:700; color:#b57a2e;">21,400 &plusmn; 350 cP</td>
                <td>19,800 &plusmn; 200 cP</td>
              </tr>
              <tr>
                <td class="col-sticky"><strong>Spreadability</strong></td>
                <td>Effortless spread (15 &ndash; 25 g&middot;cm/s)</td>
                <td>Parallel glass plate sliding extensometer</td>
                <td style="background:#fffdf7; font-weight:700; color:#1a1816;">18.75 g&middot;cm/s</td>
                <td>19.40 g&middot;cm/s</td>
              </tr>
              <tr>
                <td class="col-sticky"><strong>Homogeneity &amp; Film</strong></td>
                <td>Continuous film without streaks or voids</td>
                <td>Tactile &amp; visual slide friction test</td>
                <td style="background:#fffdf7; font-weight:600;">Complete surface homogeneity</td>
                <td>Complete surface homogeneity</td>
              </tr>
              <tr>
                <td class="col-sticky"><strong>Skin Feel (Panel n=5)</strong></td>
                <td>Non-sticky, cooling, non-greasy, non-drying</td>
                <td>Blind human panel patch assessment</td>
                <td style="background:#fffdf7; font-weight:600;"><span style="color:#059669; font-weight:600;">Non-sticky, cooling, moisturizing</span></td>
                <td>Slightly drying post-evaporation</td>
              </tr>
            </tbody>
          </table>"""

# 4. Tab 2 Commercial Benchmark HTML
tab2_benchmark_html = """<div class="marketed-reference-card">
          <h4>
            <span>&#128717;&#65039;</span>
            <span>Commercial Benchmark Comparison: Standard 2% Salicylic Acid Gel vs. Polyherbal Hydrogel F3</span>
          </h4>
          <p style="font-size: 12.5px; color:#5a534d; margin-top: 6px; line-height: 1.5;">
            Controlled side-by-side comparative analysis between synthetic monotherapy BHA gels and the novel curcuminoid-fortified polyherbal vehicle.
          </p>
          <div class="reference-pills">
            <div class="ref-pill"><span>Matrix Archetype:</span> <strong>Polyherbal Hydrogel vs. Synthetic Commercial Gel</strong></div>
            <div class="ref-pill"><span>Active Synergism:</span> <strong>2% BHA + 10% Turmeric Extract (Dual Efficacy)</strong></div>
            <div class="ref-pill"><span>Hydration Safeguard:</span> <strong>Glycerine (3%) + Sorbitol (1%) Anti-desquamation</strong></div>
            <div class="ref-pill"><span>Sensory Profile:</span> <strong>Cooling, Calming &amp; Non-staining on skin</strong></div>
          </div>
          <div style="margin-top: 14px; font-size: 12.5px; color: #5a534d; line-height: 1.55; border-left: 3px solid var(--gold-primary); padding-left: 12px;">
            <strong>Therapeutic Distinction:</strong> While standard commercial 2% salicylic acid gels induce localized xerosis, erythema, and epidermal peeling through aggressive keratolysis, Batch F3 incorporates 10% <em>Curcuma longa</em> extract to down-regulate pro-inflammatory cytokines while Glycerine and Sorbitol lock moisture into the stratum corneum.
          </div>
        </div>"""

# 5. Tab 3 Steps Grid HTML (6 Step Cards)
tab3_steps_grid_html = """<div class="step-card">
            <div class="step-number">1</div>
            <h5>Phase A: Polymer Hydration</h5>
            <p>Carbopol 940 (0.40% w/w) is slowly sprinkled uniformly over warm Purified Water and permitted to hydrate and swell for 12 hours to establish a clump-free polymer dispersion.</p>
          </div>
          <div class="step-card">
            <div class="step-number">2</div>
            <h5>Phase B: Active Solubilization</h5>
            <p>Crystalline Salicylic Acid (2.0% w/w) is completely dissolved in a co-solvent mixture of Propylene Glycol (15.0%) and Methyl Propylene Glycol (1.0%) under magnetic agitation until optically clear.</p>
          </div>
          <div class="step-card">
            <div class="step-number">3</div>
            <h5>Phase C: Botanical Incorporation</h5>
            <p>Standardized Turmeric Extract (10.0% w/w, <em>Curcuma longa</em>) is dispersed alongside Glycerine (3.0%) and Sorbitol (1.0%) into Phase B, yielding a vibrant, homogeneous curcuminoid solution.</p>
          </div>
          <div class="step-card">
            <div class="step-number">4</div>
            <h5>Phase D: Controlled Blending</h5>
            <p>Phase C is introduced into the swollen Phase A polymer dispersion under continuous low-shear mechanical stirring to homogenize without inducing unwanted air entrapment or vortex foaming.</p>
          </div>
          <div class="step-card">
            <div class="step-number">5</div>
            <h5>Phase E: TEA Neutralization</h5>
            <p>Triethanolamine (TEA) is titrated dropwise to neutralize carboxyl residues along the Carbopol backbone, expanding polymer chains into a coherent 3D viscoelastic hydrogel at pH 5.80.</p>
          </div>
          <div class="step-card">
            <div class="step-number">6</div>
            <h5>Phase F: QC &amp; Photoprotection</h5>
            <p>Rigorous characterization (centrifugation, pH electrode, Brookfield rheometer) followed by packaging into amber airless containers to shield bioactive curcuminoids against photodegradation.</p>
          </div>"""

# 6. Tab 3 Visualizer HTML
tab3_visualizer_html = """<div class="dual-action-box">
          <div class="action-side sa">
            <h6>Salicylic Acid (2.0% w/w)</h6>
            <ul>
              <li>Lipophilic Beta-Hydroxy Acid (BHA)</li>
              <li>Penetrates deep into pilosebaceous ducts</li>
              <li>Dissolves intercellular desmosomes</li>
              <li>Rapid comedolytic &amp; keratolytic clearance</li>
              <li>Co-solubilized in PG matrix to prevent crystallization</li>
            </ul>
          </div>
          <div class="action-plus">+</div>
          <div class="action-side neem" style="background: #fffdf2; border-color: #eed69b;">
            <h6 style="color: #92580c;">Curcuma longa / Turmeric (10.0% w/w)</h6>
            <ul>
              <li>Bioactive curcuminoids (curcumin, demethoxycurcumin)</li>
              <li>Suppresses NF-&kappa;B inflammatory transcription</li>
              <li>Potent antimicrobial inhibition vs <em>C. acnes</em></li>
              <li>Free-radical scavenging antioxidant barrier</li>
              <li>Humectant synergy mitigates dryness &amp; erythema</li>
            </ul>
          </div>
        </div>"""

# 7. Citations & Achievement HTML
bibtex_code = """@article{deshmukh2026formulation,
  title={Formulation, Optimization, and Comparative Evaluation of a Polyherbal Hydrogel Base Containing Salicylic Acid (2\\%) and Curcuma longa (Turmeric) Extract for Topical Applications},
  author={Deshmukh, Samruddhi Nilesh and Gahalod, Madhuri K.},
  journal={Journal of Beauty Science and Applied Cosmetology},
  volume={2},
  number={2},
  pages={1--12},
  year={2026},
  publisher={Universitas Negeri Yogyakarta},
  doi={10.21831/jbsac.v2i2},
  url={https://journal.uny.ac.id/publications/jbsac/issue/current}
}"""

apa_citation = "Deshmukh, S. N., & Gahalod, M. K. (2026). Formulation, optimization, and comparative evaluation of a polyherbal hydrogel base containing salicylic acid (2%) and Curcuma longa (turmeric) extract for topical applications. Journal of Beauty Science and Applied Cosmetology, 2(2), 1–12. https://doi.org/10.21831/jbsac.v2i2"

harvard_citation = "Deshmukh, S.N. and Gahalod, M.K., 2026. Formulation, optimization, and comparative evaluation of a polyherbal hydrogel base containing salicylic acid (2%) and Curcuma longa (turmeric) extract for topical applications. Journal of Beauty Science and Applied Cosmetology, 2(2), pp.1–12. https://doi.org/10.21831/jbsac.v2i2."

achievement_pills_html = """<a href="https://journal.uny.ac.id/publications/jbsac/issue/current" target="_blank" rel="noopener noreferrer" class="achieve-pill">&#127470;&#127465; Published from Indonesia &nearr;</a>
                <span class="achieve-pill">&#127760; International Peer-Reviewed</span>
                <a href="https://doi.org/10.21831/jbsac.v2i2" target="_blank" rel="noopener noreferrer" class="achieve-pill">&#128196; DOI: 10.21831/jbsac.v2i2 &nearr;</a>
                <span class="achieve-pill">&#127891; MGM University, Chh. Sambhajinagar</span>
                <a href="https://journal.uny.ac.id/publications/jbsac/issue/current" target="_blank" rel="noopener noreferrer" class="achieve-pill">&#128218; UNY Current Issue &nearr;</a>"""

editorial_modal_details_html = """<div><strong>Article Title:</strong> Formulation, Optimization, and Comparative Evaluation of a Polyherbal Hydrogel Base Containing Salicylic Acid (2%) and Curcuma longa (Turmeric) Extract for Topical Applications</div>
          <div style="margin-top:6px;"><strong>Lead Researcher:</strong> Samruddhi Nilesh Deshmukh (B.Tech Cosmetic Technology 3rd Year)</div>
          <div style="margin-top:6px;"><strong>Co-Author &amp; Guide:</strong> Dr. Madhuri K. Gahalod (Assistant Professor, Department of Cosmetic Technology)</div>
          <div style="margin-top:6px;"><strong>Academic Institution:</strong> MGM University, Chhatrapati Sambhajinagar, Maharashtra, India</div>
          <div style="margin-top:6px;"><strong>Journal Publisher:</strong> Universitas Negeri Yogyakarta (UNY), Indonesia &#127470;&#127465;</div>
          <div style="margin-top:6px;"><strong>Volume &amp; Issue:</strong> Vol. 2 No. 2 (2026)</div>
          <div style="margin-top:6px;"><strong>Official Journal URL:</strong> <a href="https://journal.uny.ac.id/publications/jbsac/issue/current" target="_blank" rel="noopener noreferrer" style="color:#1f4788;">https://journal.uny.ac.id/publications/jbsac/issue/current &nearr;</a></div>
          <div style="margin-top:6px;"><strong>Registered DOI:</strong> <a href="https://doi.org/10.21831/jbsac.v2i2" target="_blank" rel="noopener noreferrer" style="color:#1f4788;">https://doi.org/10.21831/jbsac.v2i2 &nearr;</a></div>
          <div style="margin-top:6px;"><strong>Certificate ID:</strong> <span style="font-family:var(--font-mono); font-weight:600;">JBSAC-V2N2-2026-SND-ID</span></div>"""

affiliations_html = """<div><sup>1</sup> <em>B.Tech Cosmetic Technology, 3rd year, MGM University, Chhatrapati Sambhajinagar, Maharashtra, India</em></div>
<div><sup>2</sup> <em>Assistant Professor, Department of Cosmetic Technology, MGM University, Chhatrapati Sambhajinagar, Maharashtra, India</em></div>"""

corresponding_authors_html = """<span><sup>*</sup>Corresponding Author / Research Guide: <a href="mailto:mgahalod@mgmu.ac.in">Dr. Madhuri K. Gahalod</a> (Assistant Professor)</span>
<span>&bull;</span>
<span>Lead Researcher: <a href="mailto:deshmukhsamruddhi85@gmail.com">Samruddhi Nilesh Deshmukh</a></span>
<span>&bull;</span>
<span>Official Issue DOI: <a href="https://doi.org/10.21831/jbsac.v2i2" target="_blank" rel="noopener noreferrer">10.21831/jbsac.v2i2 &nearr;</a></span>"""

article_dates_html = """<div><strong>Received:</strong> 15 July 2026</div>
                    <div><strong>Revised:</strong> 22 August 2026</div>
                    <div><strong>Accepted:</strong> 10 September 2026</div>
                    <div><strong>Published:</strong> October 2026</div>"""

keywords_html = """Salicylic Acid (2.0% w/w);<br>
                    Turmeric Extract (<em>Curcuma longa</em>);<br>
                    Polyherbal Hydrogel Base;<br>
                    Carbopol 940 Optimization;<br>
                    Topical Delivery Systems;<br>
                    Anti-Acne &amp; Anti-Inflammatory;<br>
                    Physicochemical &amp; Rheological Evaluation."""

abstract_html = """<p>
                      This research details the formulation design, process optimization, and comprehensive physicochemical characterization of a topical polyherbal hydrogel system containing a synergistic combination of 2.0% w/w Salicylic Acid (keratolytic active) and 10.0% w/w Turmeric Extract (<em>Curcuma longa</em>, anti-inflammatory &amp; antioxidant active). Utilizing Carbopol 940 (0.40% w/w) as a cross-linked gelling matrix, three experimental batches (F1, F2, F3) were formulated by varying co-solvent ratios and neutralizing agent concentrations to overcome the common dermatological limitations of conventional salicylic acid monotherapies.
                    </p>
                    <p>
                      The optimized formulation (F3) demonstrated superior physical stability, desirable pseudoplastic rheological flow (21,400 &plusmn; 350 cP), optimal spreadability (18.75 g&middot;cm/s), and a skin-compatible pH value of 5.80 &plusmn; 0.15. Comparative evaluation against a marketed commercial 2% salicylic acid gel control revealed superior humectant moisture retention, complete absence of crystalline precipitation under polarized microscopy, and a non-greasy, soothing post-application skin feel. The findings establish that the developed polyherbal hydrogel delivers balanced keratolytic pore-clearing efficacy while mitigating erythema and desquamation through natural curcuminoids.
                    </p>"""

caption_authors_html = """<span class="author-pill">Samruddhi Nilesh Deshmukh</span>
            <span>&bull;</span>
            <span>B.Tech Cosmetic Technology 3rd Year</span>
            <span>&bull;</span>
            <span>Dr. Madhuri K. Gahalod (Guide)</span>"""

caption_desc = "Official page proof as it appears in the <em>Journal of Beauty Science and Applied Cosmetology</em>, published by Universitas Negeri Yogyakarta (UNY), Indonesia. Official DOI registered for permanent academic verification."

data = {
    "page_title": "Samruddhi Nilesh Deshmukh — International Publication Proof | JBSAC Indonesia",
    "meta_description": "Official International Publication Proof: Formulation, Optimization, and Comparative Evaluation of a Polyherbal Hydrogel Base Containing Salicylic Acid (2%) and Curcuma longa (Turmeric) Extract for Topical Applications by Samruddhi Nilesh Deshmukh & Dr. Madhuri K. Gahalod, MGM University. Published in Journal of Beauty Science and Applied Cosmetology (JBSAC), Universitas Negeri Yogyakarta, Indonesia. DOI: 10.21831/jbsac.v2i2",
    "live_status_text": "Verified International Academic Proof • JBSAC Vol. 2 No. 2 (2026)",
    "top_bar_institution": "Universitas Negeri Yogyakarta",
    "country_name": "Indonesia",
    "country_name_upper": "INDONESIA",
    "country_code": "ID",
    "country_flag_emoji": "🇮🇩",
    "country_subtext": "Yogyakarta • Southeast Asia • International Peer-Reviewed Journal",
    "journal_url": "https://journal.uny.ac.id/publications/jbsac/issue/current",
    "journal_domain_display": "journal.uny.ac.id ↗",
    "journal_emblem_letter": "J",
    "journal_name": "Journal of Beauty Science & Applied Cosmetology",
    "journal_name_full": "Journal of Beauty Science and Applied Cosmetology",
    "journal_issue_subtitle": "Universitas Negeri Yogyakarta (UNY) Press • Vol. 2 No. 2 (2026)",
    "journal_short": "JBSAC",
    "volume": "2",
    "number": "2",
    "year": "2026",
    "page_range": "1–12",
    "publisher_name": "Universitas Negeri Yogyakarta (UNY)",
    "publisher_desc": "Yogyakarta State University Press, Indonesia",
    "publisher_short": "UNY",
    "organizer_name": "Program Studi Tata Rias dan Kecantikan, Fakultas Vokasi",
    "organizer_desc": "Cosmetology & Beauty Study Program, Faculty of Vocational Studies",
    "location_stat": "📍 Yogyakarta, Indonesia",
    "issue_stat": "Vol. 2 No. 2 (2026)",
    "hero_badge_category": "International Publication Proof",
    "hero_badge_sub": "Certified • Indonesia",
    "hero_journal_title_html": "Journal of Beauty Science<br><em>and Applied Cosmetology</em>",
    "hero_sub_bar_text": "JBSAC • Vol. 2 • No. 2 • 2026 • UNY",
    "doi": "10.21831/jbsac.v2i2",
    "doi_text": "https://doi.org/10.21831/jbsac.v2i2",
    "doi_url": "https://doi.org/10.21831/jbsac.v2i2",
    "issn_status": "Verified Standard",
    "issn_sub": "International Serial",
    "indexing_val": "Crossref DOI, Google Scholar",
    "indexing_sub": "UNY Journal Network & Garuda",
    "verification_banner_text": "This scientific article is internationally published from <strong>Yogyakarta, Indonesia</strong> by a premier state university press, indexed in Crossref with official digital object identifier (DOI: 10.21831/jbsac.v2i2), and certified for academic research attribution.",
    "seal_code": "JBSAC",
    "certificate_id": "JBSAC-V2N2-2026-SND-ID",
    "paper_title": "Formulation, Optimization, and Comparative Evaluation of a Polyherbal Hydrogel Base Containing Salicylic Acid (2%) and Curcuma longa (Turmeric) Extract for Topical Applications",
    "authors_line_html": "Samruddhi Nilesh Deshmukh<sup>1</sup>, Dr. Madhuri K. Gahalod<sup>2*</sup>",
    "affiliations_html": affiliations_html,
    "corresponding_authors_html": corresponding_authors_html,
    "article_dates_html": article_dates_html,
    "keywords_html": keywords_html,
    "abstract_html": abstract_html,
    "first_page_table_html": first_page_table_html,
    "sheet_footer_strip_html": '<span><a href="https://journal.uny.ac.id/publications/jbsac/issue/current" target="_blank" rel="noopener noreferrer">JBSAC &bull; Vol. 2 No. 2 (2026) &bull; Page Proof</a></span>\n<a href="https://doi.org/10.21831/jbsac.v2i2" target="_blank" rel="noopener noreferrer" class="doi-tag">doi: 10.21831/jbsac.v2i2 &nearr;</a>',
    "floating_stamp_text": "&#10003; Published &bull; Indonesia",
    "caption_title": "Formulation &amp; Evaluation of Polyherbal Hydrogel with Salicylic Acid &amp; Turmeric",
    "caption_authors_html": caption_authors_html,
    "caption_desc": caption_desc,
    "tab2_title": "Formulation Optimization: F1 vs. F2 vs. F3 (Carbopol 940 Matrix)",
    "tab2_sub": "Screening of gelling polymer concentration (0.30%, 0.50%, 0.40% w/w) and Triethanolamine neutralization buffer to achieve ideal pseudoplastic rheology, optimal spreadability, and a skin-compatible pH of 5.8.",
    "tab2_cards_grid_html": tab2_cards_grid_html,
    "tab2_full_table_html": tab2_full_table_html,
    "tab2_benchmark_html": tab2_benchmark_html,
    "tab3_nav_title": "Turmeric Extraction &amp; Chemistry",
    "tab3_title": "Compounding Chemistry &amp; Dual-Action Mechanism",
    "tab3_sub": "Four-phase pharmaceutical compounding protocol (Hydration, Active Solubilization, Botanical Integration, Polymer Neutralization) and dual keratolytic/anti-inflammatory pathways.",
    "tab3_steps_heading": "Standardized 4-Phase Compounding Protocol",
    "tab3_steps_grid_html": tab3_steps_grid_html,
    "tab3_visualizer_heading": "Synergistic Dual-Active Mechanism on Inflammatory Acne-Prone Skin",
    "tab3_visualizer_html": tab3_visualizer_html,
    "bibtex_code": bibtex_code,
    "apa_citation": apa_citation,
    "harvard_citation": harvard_citation,
    "author_email": "deshmukhsamruddhi85@gmail.com",
    "lead_author_name": "Samruddhi Nilesh Deshmukh",
    "achievement_avatar_letter": "S",
    "achievement_title": "Achievement Unlocked &bull; Samruddhi Nilesh Deshmukh",
    "achievement_tag": "3rd Year B.Tech Researcher",
    "achievement_lead_p": "International Journal Publication in <strong>Indonesia</strong> &bull; Journal of Beauty Science and Applied Cosmetology &bull; Universitas Negeri Yogyakarta (UNY).",
    "achievement_pills_html": achievement_pills_html,
    "achievement_loc_sub": "Yogyakarta &bull; UNY Press",
    "achievement_footer_meta": "<span>Official proof &bull; For sharing &amp; academic portfolio &bull; Not for commercial reproduction</span>\n<span style=\"font-family:var(--font-mono);\">JBSAC 2026 &bull; Verified</span>",
    "legal_disclaimer": "This visual document is crafted as an authentic publication proof &amp; academic portfolio showcase. Article content &copy; 2026 the Authors, published under open-access license by Universitas Negeri Yogyakarta (UNY). All institutional names and DOI identifiers are property of their respective registries.",
    "editorial_modal_details_html": editorial_modal_details_html
}

# Save JSON
out_dir = Path(r"d:\html pages\samruddhi")
json_path = out_dir / "samruddhi_paper_data.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"Saved {json_path}")

# Load template and generate HTML
template_content = load_template()
html_content = generate_html(data, template_content)

# Save both named html and index.html
output_html_path = out_dir / "samruddhi_deshmukh_international_proof.html"
with open(output_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Saved {output_html_path}")

index_html_path = out_dir / "index.html"
with open(index_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Saved {index_html_path}")

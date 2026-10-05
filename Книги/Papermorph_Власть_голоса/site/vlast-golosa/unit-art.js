// Chalk sketches for the unit headers on the contents page, one per unit, drawn in the unit's colour.
// Each entry is the inside of an SVG with viewBox 0 0 600 180; keep the left ~200 px light (the unit title sits there
// on narrow screens). Classes, styled in book.html:
//   d  a stroke that draws itself in when the unit scrolls into view (--k orders the strokes)
//   t  text or a filled shape that fades in
//   a  faint chalk white instead of the unit colour;  faint  even fainter
// A sketch may add one looping motion after it is drawn: give an element a class and add a .seen .unit-art .NAME
// rule with its keyframes in book.html (see the examples there: swap-a, hop, spin, tilt, breathe, ...).
'use strict';
(() => {
  let k = 0;
  const P = (d, cls = '', extra = '') => `<path class="d ${cls}" pathLength="1" style="--k:${k++}" d="${d}" ${extra}/>`;
  const Tx = (x, y, s, size = 24, cls = '', anchor = 'start') => `<text class="t ${cls}" style="--k:${k++}" x="${x}" y="${y}" font-size="${size}" text-anchor="${anchor}">${s}</text>`;
  const C = (cx, cy, r, cls = '') => `<circle class="d ${cls}" pathLength="1" style="--k:${k++}" cx="${cx}" cy="${cy}" r="${r}"/>`;
  const reset = s => { k = 0; return s; };

  const wave = (x0, x1, y, amp, cycles) => { let d = `M${x0} ${y}`; for (let i = 1; i <= 80; i++) { const x = x0 + (x1 - x0) * i / 80; d += `L${x.toFixed(1)} ${(y - amp * Math.sin(i / 80 * cycles * 2 * Math.PI)).toFixed(1)}`; } return d; };
  const block = (x, y, w, j) => `<rect class="t step" style="--k:${k++}" x="${x}" y="${y}" width="${w}" height="26" rx="8" fill="currentColor" stroke="none"/>`;
  window.UNIT_ART = [
    // 1 Голос как инструмент: связки сверху и звуковая волна, по которой бежит точка
    reset(P('M270 40C262 70 256 110 252 150M286 40C294 70 300 110 304 150', '', 'stroke-width="5"') +
      P(wave(340, 572, 95, 30, 4)) + P('M340 140H572', 'a') +
      `<circle class="t ride" r="7" fill="currentColor" stroke="none" style="--k:${k++};offset-path:path('${wave(340, 572, 95, 30, 4)}')"/>` +
      Tx(456, 40, '440 Гц', 24, 'a', 'middle')),
    // 2 Голос обольщения: низкая мягкая волна и высокая резкая, мягкая покачивается
    reset(`<g class="tilt">${P(wave(240, 572, 80, 34, 2), '', 'stroke-width="4"')}</g>` + P(wave(240, 572, 140, 12, 9), 'a') +
      Tx(560, 40, 'низко и тепло', 22, 'a', 'end')),
    // 3 Голос власти: микрофон и расходящиеся дуги
    reset(P('M300 50a22 22 0 0 1 44 0v40a22 22 0 0 1 -44 0z') + P('M290 92a32 32 0 0 0 64 0M322 124v26M300 150h44', 'a') +
      [0, 1, 2, 3].map(j => `<path class="d cell" pathLength="1" style="--k:${k++};--j:${j}" d="M${380 + j * 40} ${40 - j * 6}q${30 + j * 8} ${50 + j * 6} 0 ${100 + j * 12}"/>`).join('') +
      Tx(560, 165, 'радио · ТВ · трибуна', 20, 'a', 'end')),
    // 4 Священный голос: свод храма и отзвуки под ним
    reset(P('M250 160V80Q410 -10 570 80V160', '', 'stroke-width="4"') + P('M250 160H570', 'a') +
      [0, 1, 2].map(j => `<path class="d cell" pathLength="1" style="--k:${k++};--j:${j}" d="M${410 - 40 - j * 40} ${130 - j * 18}Q410 ${80 - j * 30} ${410 + 40 + j * 40} ${130 - j * 18}"/>`).join('') +
      Tx(410, 152, 'эхо', 20, 'a', 'middle')),
    // 5 Голос как зрелище: занавес и кукла чревовещателя, которая наклоняет голову
    reset(P('M230 20H580M240 20Q260 90 236 170M570 20Q550 90 574 170', 'a') +
      `<g class="tilt">${C(300, 72, 22)}${P('M290 70h6M304 70h6M292 84q8 6 16 0')}</g>` + P('M300 94V150M280 112h40', '') +
      Tx(470, 95, '«Кто это сказал?»', 22, '', 'middle')),
    // 6 Сила тишины: слова-блоки, пауза и знак паузы
    reset(block(240, 70, 60) + block(310, 70, 90) + block(410, 70, 70) +
      `<rect class="d" pathLength="1" style="--k:${k++}" x="490" y="70" width="44" height="26" rx="8" stroke-dasharray="1 1" />` + block(544, 70, 40) +
      P('M500 120v34M520 120v34', 'a', 'stroke-width="6"') + Tx(410, 150, 'пауза', 22, 'a', 'middle')),
  ];
})();

(()=>{'use strict';const api=window.FigureExplorer;if(!api)return;const data=api.data,$=id=>document.getElementById(id),el=(t,c,s)=>{const e=document.createElement(t);if(c)e.className=c;if(s!==undefined)e.textContent=s;return e},button=(s,fn)=>{const b=el('button','',s);b.onclick=fn;return b};
const media=matchMedia('(max-width:767px)'),land=matchMedia('(pointer:coarse) and (orientation:landscape) and (max-height:600px)'),mobile=()=>media.matches||land.matches;let trail=[],last=null,restoring=false,once=false,pending=false;
const current=el('div');current.id='mobile-current';current.setAttribute('aria-live','polite');document.querySelector('main').before(current);
const dock=el('section');dock.id='mobile-dock';dock.setAttribute('aria-label','探索する断面');document.querySelector('main').after(dock);
const row=el('div','dock-row');dock.append(row);
const close=()=>{$('detail').classList.remove('open');$('layers').classList.remove('open');$('toggle-detail').setAttribute('aria-expanded','false');$('toggle-layers').setAttribute('aria-expanded','false')};
row.append(button('Focus',()=>{api.fitFocus();close()}),button('戻る',()=>{const x=trail.pop();if(x)restore(x);close()}),button('全体',()=>{api.preset('overview');close()}),button('＋',()=>api.zoom(.82)),button('−',()=>api.zoom(1.22)),button('説明',()=>{$('detail').classList.add('open');$('layers').classList.remove('open')}),button('設定',()=>{$('layers').classList.add('open');$('detail').classList.remove('open')}),button('? 凡例',()=>help.classList.add('open')));
const form=el('div','dock-row');dock.append(form);
function selectControl(parent,label,options,fn){const l=el('label','',label),s=el('select');s.setAttribute('aria-label',label);options.forEach(([v,t])=>{const o=el('option','',t);o.value=v;s.append(o)});s.onchange=()=>fn(s.value);l.append(s);parent.append(l);return s}
const layer=selectControl(form,'何を見る？',[['relation','Relation'],['concept','Concept'],['difference','Difference'],['both','Both']],v=>{api.setBoundary({layer:v,enabled:true});close()});
const cases=data.elements.filter(e=>e.type==='example');const caseInput=selectControl(form,'どのケース？',cases.map(e=>[e.id,e.label]),v=>{api.select(v);api.setBoundary({caseId:v,enabled:true});api.fitFocus();close()});
const more=el('details');more.append(el('summary','','Σ・概念・対象を選ぶ'));dock.append(more);const selectors=el('div');selectors.id='mobile-selectors';more.append(selectors);
const sigma=selectControl(selectors,'どのΣ？',[],v=>{const b=api.getBoundary();api.setSigma(b.caseId,v);api.fitFocus();close()});const scope=selectControl(selectors,'断面',[['current','current：選択Σ'],['atlas','atlas：Σ併記']],v=>{api.setBoundary({scopeView:v,enabled:true});close()});
const concept=selectControl(selectors,'概念語',data.conceptualBoundaries.map(c=>[c.id,c.label]),v=>{api.selectConcept(v);close()});const context=selectControl(selectors,'使用文脈',Object.entries(data.usageContextLabels),v=>{api.setBoundary({context:v,enabled:true});close()});
const node=selectControl(selectors,'何を選んだ？',data.elements.filter(e=>e.type!=='path').map(e=>[e.id,e.label]),v=>api.select(v));
more.append(button('選択・レイヤーを初期化',()=>{api.mobileInitial();close()}),button('ケース比較',()=>{api.setCompare('ex-dna','ex-bacteria')}));
dock.append(el('p','','地図は分類表ではなく、監査結果を辿る探索空間です。'));
const detail=$('detail'),canonical=el('details','canonical-audit');canonical.append(el('summary','','詳しく読む：全監査・留保・比較・出典'));[$('boundary-detail'),$('detail-content')].forEach(n=>canonical.append(n));detail.append(canonical);
const summary=el('section');summary.id='mobile-audit-summary';detail.prepend(summary);const sheetClose=button('閉じる',close);sheetClose.id='mobile-sheet-close';detail.prepend(sheetClose);const settingsClose=button('閉じる',close);settingsClose.id='mobile-settings-close';$('layers').prepend(settingsClose);
const help=el('section');help.id='mobile-help';help.setAttribute('role','dialog');help.setAttribute('aria-label','凡例と横断解析');help.append(button('閉じる',()=>help.classList.remove('open')),el('h2','','凡例・操作・解析'));help.append(el('p','','● 関係概念／◆ 事例／■ 機構。参照線は含意ではありません。● 強い根拠・◐ 候補・○ 弱い・? 未確定は指定claimの根拠状態です。'));
help.append(el('p','','タップ＝選択、ドラッグ＝回転、2本指＝パン／ピンチ、ダブルタップ＝Focus。Focus・＋・−・戻るでも操作できます。ページの縦スクロールはキャンバス外で行えます。'));
help.append(el('p','','位置・距離・体積は測定値ではない。近い＝前提・類似・因果ではない。RelationとConceptは別の記述です。'));
const axes=$('axis-key').cloneNode(true);axes.removeAttribute('id');help.append(axes);data.elements.filter(e=>e.space==='panel').forEach(e=>help.append(button(e.label,()=>{help.classList.remove('open');api.select(e.id)})));document.body.append(help);
function snapshot(){const s=api.getState(),b=api.getBoundary();return{case:b.caseId,sigma:s.sigmaByExample[b.caseId],view:b.layer,scope:b.scopeView,concept:b.conceptId,context:b.context,node:s.selected,preset:s.preset,compare:s.compare,a:s.compareA,z:s.compareB}}
function restore(s){restoring=true;api.setBoundary({caseId:s.case,layer:s.view,scopeView:s.scope,conceptId:s.concept,context:s.context,enabled:true});api.setSigma(s.case,s.sigma);if(s.compare)api.setCompare(s.a,s.z);else if(s.node)api.select(s.node);else api.clearFocus();api.setBoundary({scopeView:s.scope});api.fitFocus();restoring=false;last=s;refresh()}
function detailsBlock(parent,title,text){const d=el('details');d.append(el('summary','',title),el('p','',text));parent.append(d)}
function refresh(){const s=api.getState(),b=api.getBoundary(),ctx=api.getClaimContext(),c=ctx.case,e=data.elements.find(e=>e.id===s.selected);current.textContent=`全体 ＞ ${c?.label||'ケース未指定'} ＞ ${b.scopeView==='atlas'?'atlas（各Σを併記）':ctx.mode?.label||s.sigmaByExample[b.caseId]||'Σ未指定'} ＞ ${e?.shortLabel||e?.label||'全体'}`;
 layer.value=b.layer;caseInput.value=b.caseId;scope.value=b.scopeView;concept.value=b.conceptId;context.value=b.context;node.value=s.selected||'';
 const modes=c?.sigmaModes||{};sigma.replaceChildren();Object.entries(modes).forEach(([k,v])=>{const o=el('option','',v.label||k);o.value=k;sigma.append(o)});sigma.value=s.sigmaByExample[b.caseId];
 summary.replaceChildren(el('h2','',s.compare?'ケース比較':e?.label||'全体を探索'),el('p','',s.compare?'下の全監査を開くと、Σを別々に選び比較できます。':e?.description||'ケース・Σ・関係を選択してください。'));
 summary.append(el('p','scope-note',`${c?.label||''}｜${b.scopeView==='atlas'?'Σ横断：集約せず併記':ctx.mode?.label||'Σ未指定'}。Σ変更は別の対象命題です。`));
 const records=ctx.records.filter(r=>!e||e.type==='example'||r.anchor===e.id||r.relation===e.id);summary.append(el('h3','','この断面のclaim'));
 if(!records.length)summary.append(el('p','','未設定：このケース・Σに対応するclaimは登録されていません。根拠を補完しません。'));
 records.forEach((r,i)=>{const d=el('details');if(records.length===1)d.open=true;d.append(el('summary','',`${data.evidenceLabels[r.status]||'? 未確定'}｜${r.relation}｜${r.sigma||r.scope}`),el('p','',r.basis||'根拠未指定'),el('p','',r.caveat||'留保未指定'),el('p','',`Evidence kind: ${(r.evidenceKind||[]).toString()}`));(r.references||[]).forEach(ref=>{const p=el('p'),a=el('a','',ref.label);a.href=ref.url;a.target='_blank';a.rel='noopener noreferrer';p.append(a);d.append(p)});summary.append(d)});
 detailsBlock(summary,'禁止飛躍',[...new Set([...(e?.forbiddenInferences||[]),...(c?.forbiddenInferences||[])])].join('／')||'位置の近接から含意を読まない。');
 detailsBlock(summary,'成立条件・監査上の問い',(e?.auditQuestions||[]).join('／')||'全監査の機構・Σ・対照・時間幅を確認してください。');
 summary.append(el('p','guide-note','Fo・UI・M3・N3は独立判定です。Evidenceの個数・濃さは順位を表しません。'));
 if(s.compare)canonical.open=true;
 const now=snapshot();if(last&&!restoring&&JSON.stringify(last)!==JSON.stringify(now)){trail.push(last);if(trail.length>25)trail.shift()}last=now;
 if(mobile()){const q=new URLSearchParams({view:b.layer,case:b.caseId,sigma:s.sigmaByExample[b.caseId]||'',scope:b.scopeView,concept:b.conceptId,context:b.context,node:s.selected||''});try{history.replaceState(null,'','#'+q)}catch{}}
}
window.addEventListener('explorerchange',()=>{if(!pending){pending=true;queueMicrotask(()=>{pending=false;refresh()})}});
function responsive(){const on=mobile();document.body.classList.toggle('mobile-explorer',on);canonical.open=!on;if(on&&!once){const hash=new URLSearchParams(location.hash.slice(1));api.mobileInitial();once=true;if(hash.has('case')){const c=hash.get('case');if(cases.some(e=>e.id===c)){api.setBoundary({caseId:c,layer:['relation','concept','both','difference'].includes(hash.get('view'))?hash.get('view'):'relation',enabled:true});api.setSigma(c,hash.get('sigma'));api.select(c);if(hash.get('node'))api.select(hash.get('node'));if(['current','atlas'].includes(hash.get('scope')))api.setBoundary({scopeView:hash.get('scope')});if(data.conceptualBoundaries.some(x=>x.id===hash.get('concept')))api.setBoundary({conceptId:hash.get('concept')});if(data.usageContextLabels[hash.get('context')])api.setBoundary({context:hash.get('context')});close()}}}if(!on){close();help.classList.remove('open')}setTimeout(()=>{if(on)api.fitFocus();refresh()},0)}media.addEventListener('change',responsive);land.addEventListener('change',responsive);responsive();
window.MobileExplorer={refresh,back:()=>{const s=trail.pop();if(s)restore(s)},getTrail:()=>trail.length};
})();

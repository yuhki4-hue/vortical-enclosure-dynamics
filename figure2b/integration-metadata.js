window.FIGURE2B_INTEGRATION_METADATA = {
  "chemotaxis": {
    "provenance": {
      "scope": "原著に基づく機構の監査と図2作業定義への限定的対応づけ。3D本番データは未更新。",
      "role": "提供監査JSONに由来する履歴文。現在の統合状態を表さない。"
    },
    "currentIntegration": {
      "status": "embedded",
      "embeddedClaimCount": 41,
      "sourceClaimCount": 41,
      "checker": "scripts/check_information_map.py",
      "checkerScope": "提供JSONとのsource payload一致、および41 claimsのrelation/status/evidenceKind/Σ/caveat整合",
      "theoryValidation": false,
      "browserValidation": false
    }
  }
};

(() => {
  'use strict';
  const chemotaxis = window.FIGURE_DATA?.auditSources?.chemotaxis;
  const integration = window.FIGURE2B_INTEGRATION_METADATA.chemotaxis;
  if (!chemotaxis) throw new Error('Chemotaxis audit source metadata is unavailable.');
  if (chemotaxis.scope !== integration.provenance.scope) {
    throw new Error('Chemotaxis provenance scope does not match the frozen source payload.');
  }
  chemotaxis.provenance = integration.provenance;
  chemotaxis.currentIntegration = integration.currentIntegration;
  delete chemotaxis.scope;
})();

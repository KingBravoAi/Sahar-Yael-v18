ops/k6_smoke.js
import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = { vus: 5, duration: '30s' };

export default function () {
  const params = { headers: { 'x-api-key': 'dev-key','Content-Type':'application/json' } };
  let r = http.post('http://localhost:8000/score',
    JSON.stringify({ profile:'Human-Broad', pillars:{IQ:110,EQ:105,CQ:112,AQ:108,Vision:110} }), params);
  check(r, { '200': (res) => res.status === 200 });
  sleep(1);
}

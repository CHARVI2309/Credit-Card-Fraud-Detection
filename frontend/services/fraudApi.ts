import type { Prediction, RiskLevel } from '@/data/mock'

export type PredictionRequest = {
  amount: number
  transaction_hour: number
  merchant_category: string
  foreign_transaction: boolean
  location_mismatch: boolean
  device_trust_score: number
  velocity_last_24h: number
  cardholder_age: number
}

export type PredictionResponse = {
  prediction: Prediction
  fraud_probability: number
  risk_level: RiskLevel
  recommended_action: string
  demo: boolean
}

export async function predictTransaction(input: PredictionRequest): Promise<PredictionResponse> {
  const base = input.amount > 500 ? 0.32 : 0.06
  const risk = Math.min(0.98, base + (input.foreign_transaction ? 0.18 : 0) + (input.location_mismatch ? 0.28 : 0) + Math.max(0, 70 - input.device_trust_score) / 220 + Math.max(0, input.velocity_last_24h - 5) / 45)
  const fraudProbability = Math.round(risk * 100)
  const riskLevel: RiskLevel = fraudProbability >= 70 ? 'High' : fraudProbability >= 35 ? 'Medium' : 'Low'
  return {
    prediction: fraudProbability >= 55 ? 'Fraudulent' : 'Legitimate',
    fraud_probability: fraudProbability,
    risk_level: riskLevel,
    recommended_action: fraudProbability >= 70 ? 'Block transaction and contact the cardholder.' : fraudProbability >= 35 ? 'Hold for manual review before approval.' : 'Approve transaction and continue monitoring.',
    demo: true,
  }
}

export async function predictWithApi(input: PredictionRequest) {
  const baseUrl = process.env.NEXT_PUBLIC_API_BASE_URL
  if (!baseUrl) return predictTransaction(input)
  const response = await fetch(`${baseUrl}/predict`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(input) })
  if (!response.ok) throw new Error('The fraud API is unavailable.')
  return response.json() as Promise<PredictionResponse>
}

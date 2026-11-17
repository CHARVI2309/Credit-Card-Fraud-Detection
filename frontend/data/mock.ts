export type RiskLevel = 'Low' | 'Medium' | 'High'
export type Prediction = 'Legitimate' | 'Fraudulent'

export type Transaction = {
  id: string
  amount: number
  category: 'Food' | 'Travel' | 'Electronics' | 'Grocery'
  time: string
  foreign: boolean
  probability: number
  prediction: Prediction
  status: 'Approved' | 'Blocked' | 'Review'
}

export const transactions: Transaction[] = [
  { id: 'TXN-90842', amount: 1240.5, category: 'Electronics', time: 'Today, 10:42 AM', foreign: true, probability: 94, prediction: 'Fraudulent', status: 'Blocked' },
  { id: 'TXN-90841', amount: 86.2, category: 'Grocery', time: 'Today, 10:31 AM', foreign: false, probability: 3, prediction: 'Legitimate', status: 'Approved' },
  { id: 'TXN-90840', amount: 420.0, category: 'Travel', time: 'Today, 09:58 AM', foreign: true, probability: 78, prediction: 'Fraudulent', status: 'Review' },
  { id: 'TXN-90839', amount: 34.75, category: 'Food', time: 'Today, 09:42 AM', foreign: false, probability: 2, prediction: 'Legitimate', status: 'Approved' },
  { id: 'TXN-90838', amount: 730.0, category: 'Electronics', time: 'Today, 09:17 AM', foreign: false, probability: 64, prediction: 'Fraudulent', status: 'Review' },
  { id: 'TXN-90837', amount: 219.9, category: 'Grocery', time: 'Yesterday, 08:52 PM', foreign: false, probability: 7, prediction: 'Legitimate', status: 'Approved' },
  { id: 'TXN-90836', amount: 68.4, category: 'Food', time: 'Yesterday, 08:21 PM', foreign: false, probability: 4, prediction: 'Legitimate', status: 'Approved' },
]

export const activityData = [
  { day: 'Mon 12', legitimate: 4200, fraud: 92 }, { day: 'Tue 13', legitimate: 5100, fraud: 124 }, { day: 'Wed 14', legitimate: 4700, fraud: 86 }, { day: 'Thu 15', legitimate: 6200, fraud: 148 }, { day: 'Fri 16', legitimate: 5800, fraud: 112 }, { day: 'Sat 17', legitimate: 3900, fraud: 74 }, { day: 'Sun 18', legitimate: 4600, fraud: 98 },
]

export const categoryData = [
  { name: 'Food', value: 118 }, { name: 'Grocery', value: 76 }, { name: 'Travel', value: 64 }, { name: 'Electronics', value: 52 },
]

export const amountData = [
  { range: '$0–100', fraud: 22, legitimate: 74 }, { range: '$100–500', fraud: 41, legitimate: 54 }, { range: '$500–1k', fraud: 28, legitimate: 25 }, { range: '$1k+', fraud: 13, legitimate: 9 },
]

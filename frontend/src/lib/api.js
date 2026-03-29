const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api';

async function request(path, options = {}) {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {}),
    },
    ...options,
  });

  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    throw new Error(data.error || 'Request failed.');
  }

  return data;
}

export function evaluateDecision(payload) {
  return request('/decisions/evaluate/', {
    method: 'POST',
    body: JSON.stringify(payload),
  });
}

export function sendChatMessage(message) {
  return request('/chat/', {
    method: 'POST',
    body: JSON.stringify({ message }),
  });
}

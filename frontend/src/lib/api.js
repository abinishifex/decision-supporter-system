const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api';

async function request(path, options = {}) {
  let response;

  try {
    response = await fetch(`${API_BASE_URL}${path}`, {
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      ...options,
    });
  } catch (error) {
    throw new Error('Unable to reach the backend. Make sure Django is running on http://localhost:8000.');
  }

  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    throw new Error(data.error || data.detail || 'Request failed.');
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

export function loginUser(credentials) {
  return request('/auth/login/', {
    method: 'POST',
    body: JSON.stringify(credentials),
  });
}

export function registerUser(payload) {
  return request('/auth/register/', {
    method: 'POST',
    body: JSON.stringify(payload),
  });
}

export function logoutUser() {
  return request('/auth/logout/', {
    method: 'POST',
  });
}

export function getCurrentUser() {
  return request('/auth/me/');
}

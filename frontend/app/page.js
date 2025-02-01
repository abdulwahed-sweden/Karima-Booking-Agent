"use client";

import { useEffect, useState } from 'react';
import api from './api';

export default function HomePage() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    api.get('/api/').then((response) => {
      setMessage(response.data.message || 'Welcome!');
    });
  }, []);

  return (
    <main className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="bg-white p-8 shadow-md rounded-lg text-center">
        <h1 className="text-2xl font-bold text-gray-800">{message}</h1>
        <p className="text-gray-600 mt-4">Manage your translation bookings seamlessly.</p>
      </div>
    </main>
  );
}

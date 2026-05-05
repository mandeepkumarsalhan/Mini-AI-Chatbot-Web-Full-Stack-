import React from 'react';

const ChatHeader: React.FC = () => {
  return (
    <header className="w-full p-4 glass-morphism sticky top-0 z-10 flex items-center justify-between">
      <div className="flex items-center gap-3">
        <div className="w-10 h-10 rounded-full bg-gradient-to-tr from-indigo-500 to-purple-500 flex items-center justify-center shadow-lg shadow-indigo-500/20">
          <span className="text-xl">🤖</span>
        </div>
        <div>
          <h1 className="font-bold text-lg text-white leading-none">Mini AI</h1>
          <span className="text-xs text-emerald-400 flex items-center gap-1">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
            Online
          </span>
        </div>
      </div>
      <button 
        onClick={() => window.location.reload()}
        className="p-2 hover:bg-white/10 rounded-lg transition-colors text-slate-400 hover:text-white"
        title="Reset Conversation"
      >
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>
      </button>
    </header>
  );
};

export default ChatHeader;

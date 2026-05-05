import React from 'react';

type MessageProps = {
  sender: "user" | "bot";
  text: string;
};

const ChatMessage: React.FC<MessageProps> = ({ sender, text }) => {
  const isBot = sender === "bot";

  return (
    <div className={`flex w-full ${isBot ? 'justify-start' : 'justify-end'} mb-4 animate-in fade-in slide-in-from-bottom-2 duration-300`}>
      <div className={`max-w-[80%] px-4 py-3 rounded-2xl shadow-sm ${
        isBot 
          ? 'bg-slate-800 text-slate-200 rounded-tl-none border border-slate-700' 
          : 'bg-indigo-600 text-white rounded-tr-none shadow-indigo-500/20'
      }`}>
        <p className="text-sm md:text-base leading-relaxed break-words whitespace-pre-wrap">
          {text}
        </p>
      </div>
    </div>
  );
};

export default ChatMessage;

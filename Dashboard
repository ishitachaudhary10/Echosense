import { useNavigate } from 'react-router-dom';

// Header Component
const Header = () => {
  return (
    <header className="bg-gradient-to-r from-[#75625E] to-[#E0A295] text-white p-6 sticky top-0 z-10 shadow-lg w-full">
      <div className="flex justify-between items-center px-8">
        <h1 className="text-3xl font-bold tracking-wide">Echosense</h1>
        <nav>
          <ul className="flex space-x-6">
            <li>
              <a href="#about" className="text-white hover:text-[#F0DEDC] transition-colors duration-300">
                About
              </a>
            </li>
            <li>
              <a href="#features" className="text-white hover:text-[#F0DEDC] transition-colors duration-300">
                Features
              </a>
            </li>
            <li>
              <a href="#testimonials" className="text-white hover:text-[#F0DEDC] transition-colors duration-300">
                How It Works
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

// Footer Component
const Footer = () => {
  return (
    <footer className="bg-gradient-to-r from-[#75625E] to-[#E0A295] text-white p-6 text-center shadow-lg w-full">
      <div className="flex flex-col items-center">
        <p>&copy; 2025 Echosense. All rights reserved.</p>
        <ul className="flex space-x-6 mt-4">
          <li>
            <a href="#" className="text-white hover:text-[#F0DEDC] transition-colors duration-300">
              Terms of Service
            </a>
          </li>
          <li>
            <a href="#" className="text-white hover:text-[#F0DEDC] transition-colors duration-300">
              Privacy Policy
            </a>
          </li>
        </ul>
      </div>
    </footer>
  );
};

// Dashboard Component
const Dashboard = () => {
  const navigate = useNavigate();

  const modules = [
    {
      title: 'ASL Alphabet to Speech',
      description: 'Convert ASL alphabet signs to spoken words',
      path: '/asl-alphabet',
      icon: '🤟',
      color: '#FFC107',
    },
    {
      title: 'Sign Language Words to Speech',
      description: 'Convert complete sign language words to speech',
      path: '/sign-language-words',
      icon: '👐',
      color: '#8BC34A',
    },
    {
      title: 'Speech-to-Speech Translation',
      description: 'Translate and speak in multiple languages',
      path: '/speech-translation',
      icon: '🗣️',
      color: '#03A9F4',
    },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-[#F0DEDC] to-[#E0A295] flex flex-col items-center overflow-hidden">
      <Header />
      
      {/* Hero Section */}
      <section className="max-w-7xl mx-auto w-full flex-1 p-8 text-center">
        <h1 className="text-6xl font-bold text-[#75625E] mb-16 tracking-wide drop-shadow-lg">
        EchoSense
        </h1>
         <h3 className="text-6xl font-bold text-[#75625E] mb-16 tracking-wide drop-shadow-lg">
        Sense. Speak. Empower.
        </h3>
        <p className="text-lg text-[#7F9AA5] mb-12">
          Bridging communication gaps with innovative solutions for sign language and speech translation.
        </p>

        {/* Modules Section */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-8">
          {modules.map((module) => (
            <button
              key={module.path}
              onClick={() => navigate(module.path)}
              className={`relative bg-white p-8 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 group overflow-hidden`}
              style={{ borderTop: `6px solid ${module.color}` }}
            >
              {/* Decorative Background */}
              <div
                className={`absolute inset-0 bg-[${module.color}] opacity-10 group-hover:opacity-20 transition-opacity duration-300`}
              ></div>

              {/* Content */}
              <div className="relative z-10">
                <div className="text-[4rem] mb-4">{module.icon}</div>
                <h2 className="text-xl font-semibold text-[#75625E] mb-2 group-hover:text-[#E0A295] transition-colors duration-300">
                  {module.title}
                </h2>
                <p className="text-[#7F9AA5]">{module.description}</p>
              </div>

              {/* Hover Effect */}
              <div
                className={`absolute bottom-0 left-0 w-full h-[6px] bg-[${module.color}] group-hover:h-[12px] transition-all duration-300`}
              ></div>
            </button>
          ))}
        </div>
      </section>

      {/* About Section */}
      <section id="about" className="max-w-7xl mx-auto w-full p-8 mt-16 text-center bg-white rounded-xl shadow-lg">
        <h2 className="text-4xl font-bold text-[#75625E] mb-8">About Us</h2>
        <p className="text-lg text-[#7F9AA5] leading-relaxed">
          At Echosense, we are committed to revolutionizing communication by developing tools that empower individuals 
          with diverse needs. Our platform bridges the gap between sign language and spoken language, making communication seamless and accessible for everyone.
        </p>
      </section>

      {/* Features Section */}
      <section id="features" className="max-w-full bg-gradient-to-r from-[#75625E] to-[#E0A295] text-white py-16 mt-16 text-center shadow-lg w-full px-[10%]">
        <h2 className="text-4xl font-bold mb-8">Features</h2>
        <ul className="space-y-6 text-lg leading-relaxed">
          <li>✔️ Real-time translation of ASL alphabet into speech.</li>
          <li>✔️ Advanced AI-powered sign language word recognition.</li>
          <li>✔️ Multilingual speech-to-speech translation capabilities.</li>
          <li>✔️ Intuitive and user-friendly interface for all users.</li>
        </ul>
      </section>

    
{/* How It Works Section */}
<section id="how-it-works" className="max-w-7xl mx-auto w-full p-8 mt-16 mb-16 text-center bg-white rounded-xl shadow-lg">
  <h2 className="text-4xl font-bold text-[#75625E] mb-8">How It Works</h2>
  <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
    <div className="bg-[#F7F7F7] p-6 rounded-lg shadow-md">
      <h3 className="text-lg font-bold text-[#75625E] mb-4">Step 1: Sign Language Input</h3>
      <p className="text-lg text-[#7F9AA5] leading-relaxed">
        Use our intuitive interface to input sign language gestures or words.
      </p>
    </div>
    <div className="bg-[#F7F7F7] p-6 rounded-lg shadow-md">
      <h3 className="text-lg font-bold text-[#75625E] mb-4">Step 2: AI-Powered Translation</h3>
      <p className="text-lg text-[#7F9AA5] leading-relaxed">
        Our advanced AI technology translates the input into spoken language in real-time.
      </p>
    </div>
    <div className="bg-[#F7F7F7] p-6 rounded-lg shadow-md">
      <h3 className="text-lg font-bold text-[#75625E] mb-4">Step 3: Output and Feedback</h3>
      <p className="text-lg text-[#7F9AA5] leading-relaxed">
        Receive the translated output and provide feedback to improve future translations.
      </p>
    </div>
  </div>
</section>


      <Footer />
    </div>
  );
};

export default Dashboard;

import React, { useRef, useEffect, useState } from 'react';
import { Hands } from '@mediapipe/hands';
import { Camera } from '@mediapipe/camera-utils';

function App() {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const [detectedWords, setDetectedWords] = useState([]);
  const [isWebcamActive, setIsWebcamActive] = useState(false);
  const cameraRef = useRef(null);

  const gestureMap = {
    "01000": "One",
    "01100": "Two",
    "11111": "Hello",
    "01111": "Thank You",
  };

  // Convert landmarks to fingers up binary string
  const getFingerPattern = (landmarks) => {
    if (!landmarks || landmarks.length === 0) return "";

    // Tip IDs: Thumb = 4, Index = 8, Middle = 12, Ring = 16, Pinky = 20
    const tips = [4, 8, 12, 16, 20];
    const pattern = tips.map((tipId, i) => {
      if (i === 0) {
        return landmarks[tipId].x < landmarks[tipId - 1].x ? 1 : 0; // Thumb (x-axis)
      } else {
        return landmarks[tipId].y < landmarks[tipId - 2].y ? 1 : 0; // Fingers (y-axis)
      }
    });
    return pattern.join("");
  };

  useEffect(() => {
    const hands = new Hands({
      locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`,
    });

    hands.setOptions({
      maxNumHands: 1,
      minDetectionConfidence: 0.7,
      minTrackingConfidence: 0.7,
    });

    hands.onResults((results) => {
      const canvas = canvasRef.current;
      const ctx = canvas.getContext("2d");

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(results.image, 0, 0, canvas.width, canvas.height);

      if (results.multiHandLandmarks && results.multiHandLandmarks.length > 0) {
        const pattern = getFingerPattern(results.multiHandLandmarks[0]);
        const word = gestureMap[pattern];
        if (word) {
          setDetectedWords((prev) => {
            if (prev[prev.length - 1] !== word) return [...prev, word];
            else return prev;
          });
        }
      }
    });

    if (isWebcamActive && !cameraRef.current) {
      cameraRef.current = new Camera(videoRef.current, {
        onFrame: async () => {
          await hands.send({ image: videoRef.current });
        },
        width: 640,
        height: 480,
      });
      cameraRef.current.start();
    }

    return () => {
      if (cameraRef.current) {
        cameraRef.current.stop();
        cameraRef.current = null;
      }
    };
  }, [isWebcamActive]);

  return (
    <div className="flex flex-col items-center p-4">
      <h1 className="text-2xl font-bold mb-4">Sign Language Word Detector</h1>

      <div className="relative w-[640px] h-[480px]">
        <video ref={videoRef} className="absolute top-0 left-0 w-full h-full" autoPlay playsInline muted />
        <canvas ref={canvasRef} className="absolute top-0 left-0 w-full h-full" />
      </div>

      <button
        onClick={() => setIsWebcamActive(!isWebcamActive)}
        className="mt-4 px-4 py-2 bg-blue-600 text-white rounded-xl shadow-md hover:bg-blue-700"
      >
        {isWebcamActive ? "Stop" : "Start"} Detection
      </button>

      <div className="mt-6 text-lg text-center">
        <h2 className="font-semibold mb-2">Detected Words:</h2>
        <ul className="list-disc list-inside">
          {detectedWords.map((word, idx) => (
            <li key={idx}>{word}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;

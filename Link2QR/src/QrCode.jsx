import { useState } from "react";
import './App.css';

export const QrCode = () => {
   const [img,setImg]= useState("");
   const [loading,setLoading]=useState(false);
   const[qrData,setQrData] =useState("");
   const[qrSize,setQrSize] =useState("");
   const [error, setError] = useState("");
   const [success, setSuccess] = useState("");


   const isValidUrl = (string) => {
      try {
         new URL(string);
         return true;
      } catch (_) {
         return false;
      }
   };


   const validateInputs = () => {
      if (!qrData.trim()) {
         setError("Please enter a URL");
         return false;
      }
      
      if (!isValidUrl(qrData)) {
         setError("Please enter a valid URL (e.g., https://example.com)");
         return false;
      }
      
      if (!qrSize || qrSize < 50 || qrSize > 300) {
         setError("QR size must be between 50 and 300 pixels");
         return false;
      }
      
      setError("");
      return true;
   };

    async function generateQR(){
       if (!validateInputs()) return;
       
       setLoading(true);
       setError("");
       setSuccess("");
       
       try{
        const url =`https://api.qrserver.com/v1/create-qr-code/?size=${qrSize}x${qrSize}&data=${encodeURIComponent(qrData)}`;
        setImg(url);
        
        // Delay success message until after image loads
        setTimeout(() => {
            setSuccess("QR Code generated successfully!");
            setTimeout(() => setSuccess(""), 3000);
        }, 500);

       }catch(error){
        console.error("Error generating QR code",error);
        setError("Failed to generate QR code. Please try again.");

       }finally{
        setLoading(false);
       }
    }
    
    function downloadQr(){
        try{
                fetch(img).then((response)=>response.blob()).then((blob)=>{
                    const link=document.createElement("a");
                    link.href=URL.createObjectURL(blob);
                    link.download="qrcode.png";
                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);
                    setSuccess("QR Code downloaded successfully!");
                    setTimeout(() => setSuccess(""), 3000);
                });
             }
            catch(error){
                console.error("Error in Downloading QRcode",error);
                setError("Failed to download QR code. Please try again.");
            };
    }

    function clearForm() {
        setQrData("");
        setQrSize("");
        setImg("");
        setError("");
        setSuccess("");
    }

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            generateQR();
        }
    };

  return (
    <div className="main">
        <div className="app-container">
            {error && <div className="error-message">{error}</div>}
            {success && <div className="success-message">{success}</div>}
            
            <div className="inputs">
                <label htmlFor="dataInput" className="input-label">
                URL:
            </label>
            <input 
                id="dataInput"
                type="text" 
                className="field" 
                value={qrData} 
                placeholder="https://www.example.com" 
                onChange={(e)=>setQrData(e.target.value)}
                onKeyPress={handleKeyPress}
                autoFocus
            />
            <label htmlFor="sizeInput" className="input-label">
            QR Size (50-300px):    
            </label>
            <input 
                id="sizeInput"
                type="number" 
                className="field size-field" 
                value={qrSize} 
                placeholder="300"
                min="100"
                max="1000"
                onChange={(e)=>setQrSize(e.target.value)}
                onKeyPress={handleKeyPress}
            />
            
            <div className="size-presets">
                <button type="button" className="preset-btn" onClick={() => setQrSize("50")}>Small</button>
                <button type="button" className="preset-btn" onClick={() => setQrSize("150")}>Medium</button>
                <button type="button" className="preset-btn" onClick={() => setQrSize("300")}>Large</button>
            </div>
            </div>
            
            <div className="buttons">
                <button className="generate-button" disabled={loading} onClick={generateQR}>
                    {loading ? "Generating..." : "Generate QR Code"}
                </button>
                <button className="clear-button" onClick={clearForm} disabled={loading}>
                    Clear
                </button>
            </div>
        </div>
        <div className="qr-code">
            {loading && (
                <div className="loading-container">
                    <div className="spinner"></div>
                    <p>Generating QR Code...</p>
                </div>
            )}
            {!loading && img && (
                <div className="qr-display">
                    <img src={img} className="qr-code-image" alt="Generated QR Code" />
                    <button className="download-button" onClick={downloadQr}>Download QR Code</button>
                </div>
            )}
            {!loading && !img && <p className="placeholder-text">Generated QR Code</p>}
        </div>
    </div>

  )
}

export default QrCode;
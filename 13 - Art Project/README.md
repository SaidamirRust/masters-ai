
# Generative AI Capstone Project: Redesigning Iconic Media Covers  
**Objective**: Create AI-generated variations of three iconic covers using a self-hosted ComfyUI workflow.  

---

## 1. Original Works & AI Variations  

### **1.1 "20,000 Leagues Under the Sea" (Jules Verne Book Cover)**  
**Original**:  
![Original Cover](jules_verne_original.jpg)  
*(Classic 19th-century illustration of the Nautilus submarine with tentacles)*  

**AI Variation**:  
![Nautilus](jules_verne_ai.png)  

---

### **1.2 "Necron Codex" by Jaime Martinez (Warhammer 40K Cover Art)**  
**Original**:  
![Original Necron Art](jaime-martinez-necrons-codex-original.jpg)  
*(Grimdark sci-fi artwork of a Necron army awakening)*  

**AI Variation**:  
![Cyberpunk Necron](jaime-martinez-necrons-codex-ai.png)  

---

### **1.3 Pink Floyd – "Dark Side of the Moon" (Vinyl Album Cover)**  
**Original**:  
![Original Pink Floyd Cover](Dark_Side_of_the_Moon_Original.jpg)  
*(Prism refracting light into a rainbow on black background)*  

**AI Variation**:  
![Bioluminescent Prism](Dark_Side_of_the_Moon_AI.png)  

---

## 2. Workflow Documentation  

### **Technical Setup**  
| Component           | Details                                                                 |
|---------------------|-------------------------------------------------------------------------|
| **Tool**            | ComfyUI (self-hosted, offline)                     |
| **Base Model**      | `v1-5-pruned-emaonly-fp16.safetensors` |
| **OS**      | Windows 11                                |
| **Hardware**        | NVIDIA GeForce RTX 4060 GPU (32GB RAM)                                              |

### **Generation Parameters**  
- **Different for each Cover. Details are specified in the Workflow section of each Cover Art;**

---

## 3. Workflow Screenshots 

### **ComfyUI Node Graphs**  
1. **Jules Verne Book Cover**:  
   ![Jules Verne Workflow]((jules_verne_prompt.png))  

2. **Necron Art Modification**:  
   ![Necron Workflow](jaime-martinez-necrons-codex-prompt.png)  

3. **Vinyl Art Variation**:  
   ![Pink Floyd Workflow](Dark_Side_of_the_Moon_Prompt.png)  

---

## 4. Assets & References  
- **Original Images**:  
  - [Jules Verne Cover Source](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.com%2F20-000-Leagues-Under-Sea%2Fdp%2F0553212524&psig=AOvVaw0BWlmE6aB0pjPoMujTTB5o&ust=1745694948156000&source=images&cd=vfe&opi=89978449&ved=0CBcQjhxqFwoTCJDH587y84wDFQAAAAAdAAAAABAE)  
  - [Necron Codex Cover Source](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.warhammerart.com%2Fproducts%2Fcodex-necrons-cover-art-10th-edition&psig=AOvVaw3Hwxv8gyk5TVCFIybhiyJj&ust=1745695038893000&source=images&cd=vfe&opi=89978449&ved=0CBcQjhxqFwoTCJCBsPby84wDFQAAAAAdAAAAABAE)  
  - [Pink Floyd Album Cover Source]([https://example.com/pink_floyd](https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FThe_Dark_Side_of_the_Moon&psig=AOvVaw0eaZ5yXzvKNXFFsx57yid9&ust=1745695095062000&source=images&cd=vfe&opi=89978449&ved=0CBcQjhxqFwoTCPDjhJLz84wDFQAAAAAdAAAAABAE))  

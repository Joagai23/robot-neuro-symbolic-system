using System;
using System.IO;
using UnityEngine;
using System.Net.Http;
using System.Text;
using System.Linq;
using RosMessageTypes.NiryoMoveit;
using System.Threading.Tasks;

public class ScreenShot : MonoBehaviour
{
    public Camera[] cams;
    public GameObject[] jars;

    public GameObject quickJar;

    // Variables required for REST communication
    private readonly string m_ServerUri = "http://localhost:8080/api/capture_perception";
    private HttpClient m_HttpClient;
    private byte[] m_Image;

    private TrajectoryPlanner m_TrajectoryPlanner;

    private void Start()
    {
        m_HttpClient = new HttpClient();
        m_TrajectoryPlanner = GetComponent<TrajectoryPlanner>();
    }

    private async Task<bool> Screenshot(string bottleId, Camera cam)
    {
        // Capture screen image and transform into byte[]
        m_Image = CaptureScreen(bottleId, cam);

        // Create Request Body
        ScreenshotRequest requestBody = new() { image = m_Image, camera = cam.name, jar = bottleId};
        string jsonData = JsonUtility.ToJson(requestBody, true);

        // Send POST Request
        var httpContent = new StringContent(jsonData, Encoding.UTF8, "application/json");
        await m_HttpClient.PostAsync(m_ServerUri, httpContent);
        //string responseString = await response.Content.ReadAsStringAsync();

        return true;
    }

    // Call from Scene UI
    public async void IterateBottles()
    {
        // Iterate Jars
        foreach (GameObject jar in jars)
        {
            // Show the object
            jar.SetActive(true);

            // Iterate Cameras
            foreach(Camera cam in cams)
            {
                // Post Screenshot
                await Screenshot(jar.name, cam);
            }

            // Hide the object
            jar.SetActive(false);
        }
    }

    public async void QuickIteration()
    {
        // Iterate Cameras
        foreach (Camera cam in cams)
        {
            // Post Screenshot
            await Screenshot(quickJar.name, cam);
        }
    }

    public void PublishROSTopic(ScreenshotResponse screenshotResponse)
    {
        // Define rotation variable in radians
        float rotationAngles = -1.0f;

        // Define rotation angles depending on the affordances
        if (screenshotResponse.affordances.Contains("Affordance:Unscrew"))
        {
            // 360º
            rotationAngles = 2 * Mathf.PI;
        }
        else if (screenshotResponse.affordances.Contains("Affordance:Lift"))
        {
            rotationAngles = 0.0f;
        }

        if(rotationAngles >= 0.0f)
        {
            
        }
        m_TrajectoryPlanner.PublishJoints(rotationAngles);
    }

    public byte[] CaptureScreen(string bottleId, Camera cam)
    {
        // Prepare RenderTexture for camera
        RenderTexture screenTexture = new(Screen.width, Screen.height, 16);
        cam.targetTexture = screenTexture;
        RenderTexture.active = screenTexture;
        cam.Render();

        // Copy camera render to RenderTexture
        Texture2D renderedTexture = new(Screen.width, Screen.height);
        renderedTexture.ReadPixels(new Rect(0, 0, Screen.width, Screen.height), 0, 0);
        RenderTexture.active = null;

        // Encode render to byte array
        byte[] jpgArray = renderedTexture.EncodeToJPG();
        string fileName = string.Concat(bottleId, '-', cam.name);
        string jpgPath = Application.dataPath + "/Images/RobotJars/" + fileName + ".jpg";

        // Save rendered image
        //File.WriteAllBytes(jpgPath, jpgArray);

        return jpgArray;
    }
}

[Serializable]
public class ScreenshotRequest
{
    public byte[] image;
    public string camera;
    public string jar;
}

[Serializable]
public class ScreenshotResponse
{
    public string[] affordances;
    public string caption;

    public string GetAffordances()
    {
        string affordanceString = "";
        foreach(string affordance in affordances)
        {
            affordanceString += affordance + ", ";
        }

        return affordanceString;
    }
}

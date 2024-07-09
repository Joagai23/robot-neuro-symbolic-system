using System.Collections;
using UnityEngine;

public class TwistRobot : MonoBehaviour
{
    public GameObject robot;
    public GameObject lid;
    public float rotationSpeed = 100.0f;

    private Transform HandLink = null;
    private GameObject RobotCopy;
    private GameObject LidCopy;

    public void DuplicateRobot()
    {
        // Duplicate Robot and Hide it
        RobotCopy = Duplicate(robot.transform.parent, robot);
        LidCopy = Duplicate(lid.transform.parent, lid);

        MakeVisibleRecursive(robot.transform, false);
        MakeVisibleRecursive(lid.transform, false);

        // Find Robot Hand Link
        HandLink = RobotCopy.transform.Find("world/base_link/shoulder_link/arm_link/elbow_link/forearm_link/wrist_link/hand_link");
        if (HandLink != null)
        {
            HandLink.SetParent(LidCopy.transform);
        }
        StartCoroutine(RotateObjectCoroutine());
    }

    public void GetGameObjectPath(GameObject obj)
    {
        string path = "/" + obj.name;
        while (obj.transform.parent != null)
        {
            obj = obj.transform.parent.gameObject;
            path = "/" + obj.name + path;
        }
        Debug.Log(path);
    }

    GameObject Duplicate(Transform parent, GameObject original)
    {
        // Create a new GameObject as a copy of the original
        GameObject copy = new GameObject(original.name);

        // Set the parent of the copy
        copy.transform.SetParent(parent);

        // Copy the transform of the original
        copy.transform.position = original.transform.position;
        copy.transform.rotation = original.transform.rotation;
        copy.transform.localScale = original.transform.localScale;

        // Copy the mesh filter if it exists
        MeshFilter meshFilter = original.GetComponent<MeshFilter>();
        if (meshFilter != null)
        {
            MeshFilter copyMeshFilter = copy.AddComponent<MeshFilter>();
            copyMeshFilter.mesh = meshFilter.sharedMesh;
        }

        // Copy the mesh renderer if it exists
        MeshRenderer meshRenderer = original.GetComponent<MeshRenderer>();
        if (meshRenderer != null)
        {
            copy.AddComponent<MeshRenderer>().sharedMaterials = meshRenderer.sharedMaterials;
        }

        // Loop through all the children of the original GameObject
        foreach (Transform child in original.transform)
        {
            // Recursively duplicate each child
            Duplicate(copy.transform, child.gameObject);
        }

        return copy;
    }

    IEnumerator RotateObjectCoroutine()
    {
        float currentRotation = 0f;
        while (currentRotation < 360f)
        {
            float rotationAmount = rotationSpeed * Time.deltaTime;
            LidCopy.transform.Rotate(0f, 0f, rotationAmount);
            currentRotation += rotationAmount;
            yield return null;
        }
        // Ensure that the object finishes exactly at 360 degrees
        LidCopy.transform.rotation = Quaternion.Euler(0f, 0f, 360f);
        UnhideRobot();
    }

    private void UnhideRobot()
    {
        // Destroy Copies
        Destroy(LidCopy);
        Destroy(RobotCopy);

        // Unhide Original Physics Robot
        MakeVisibleRecursive(robot.transform, true);
        MakeVisibleRecursive(lid.transform, true);
    }
    void MakeVisibleRecursive(Transform trans, bool renderEnabled)
    {
        // Disable the renderer component on this object
        Renderer rend = trans.GetComponent<Renderer>();
        if (rend != null)
        {
            rend.enabled = renderEnabled;
        }

        // Recursively disable renderer component on children
        foreach (Transform child in trans)
        {
            MakeVisibleRecursive(child, renderEnabled);
        }
    }
}

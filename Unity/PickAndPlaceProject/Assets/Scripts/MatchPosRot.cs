using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MatchPosRot : MonoBehaviour
{
    public Transform targetObject;

    private Vector3 initialPositionDifference;
    private Quaternion initialRotationDifference;

    void Start()
    {
        // Calculate initial position and rotation differences
        if (targetObject != null)
        {
            // Calculate position difference
            initialPositionDifference = transform.position - targetObject.position;

            // Calculate rotation difference except for rotation around the Y axis
            Quaternion targetRotationWithoutY = Quaternion.Euler(0f, targetObject.rotation.eulerAngles.y, 0f);
            Quaternion currentRotationWithoutY = Quaternion.Euler(0f, transform.rotation.eulerAngles.y, 0f);
            initialRotationDifference = Quaternion.Inverse(targetRotationWithoutY) * currentRotationWithoutY;
        }
    }

    void LateUpdate()
    {
        if (targetObject != null)
        {
            // Apply the initial position and rotation differences
            transform.position = targetObject.position + initialPositionDifference;
            Quaternion targetRotationWithoutY = Quaternion.Euler(0f, targetObject.rotation.eulerAngles.y, 0f);
            transform.rotation = targetRotationWithoutY * initialRotationDifference;
        }
    }
}

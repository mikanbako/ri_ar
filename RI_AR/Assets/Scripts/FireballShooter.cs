/* Copyright (c) 2016 Keita Kita
 *
 * This software is released under the MIT License.
 * http://opensource.org/licenses/mit-license.php
 */

using UnityEngine;
using Vuforia;

public sealed class FireballShooter : MonoBehaviour
{
    [SerializeField]
    private GameObject _remoteController;

    [SerializeField]
    private GameObject _startPositionBase;

    [SerializeField]
    private GameObject _fireballPrefab;

    private bool IsRemoteControllerTracking()
    {
        var remoteControllerRenderer = _remoteController
            .GetComponentsInChildren<Renderer>();

        return remoteControllerRenderer[0].enabled;
    }

    public void Shoot()
    {
        if (!IsRemoteControllerTracking())
        {
            return;
        }

        var fireballObject = (GameObject) Instantiate(
            _fireballPrefab,
            _startPositionBase.transform.position,
            Quaternion.Euler(new Vector3(0, -90, 0)));

        var fireball =
            fireballObject.GetComponent<ParticleSystem>();

        fireball.Play();
    }
}

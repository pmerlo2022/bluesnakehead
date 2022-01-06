# AMS

# Table of Contents
<!-- toc -->

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

<!-- toc -->
# Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision |
| --- | ---- | ---- | ------------- | -------- | -------------------------- |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF1A | 10.6.1.20/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF1B | 10.6.1.21/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF2A | 10.6.1.22/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF2B | 10.6.1.23/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF3A | 10.6.1.24/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF3B | 10.6.1.25/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF4A | 10.6.1.26/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF4B | 10.6.1.27/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF5A | 10.6.1.28/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF5B | 10.6.1.29/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF6A | 10.6.1.30/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF6B | 10.6.1.31/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF7A | 10.6.1.32/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF7B | 10.6.1.33/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF8A | 10.6.1.34/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF8B | 10.6.1.35/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF9A | 10.6.1.36/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF9B | 10.6.1.37/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF10A | 10.6.1.38/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF10B | 10.6.1.39/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF11A | 10.6.1.40/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF11B | 10.6.1.41/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF12A | 10.6.1.42/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF12B | 10.6.1.43/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF13A | 10.6.1.44/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF13B | 10.6.1.45/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF14A | 10.6.1.46/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF14B | 10.6.1.47/24 | 7280R | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE1 | 10.6.1.10/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE2 | 10.6.1.11/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE3 | 10.6.1.12/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE4 | 10.6.1.13/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF1A | 10.6.33.20/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF1B | 10.6.33.21/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF2A | 10.6.33.22/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF2B | 10.6.33.23/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF3A | 10.6.33.24/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF3B | 10.6.33.25/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF4A | 10.6.33.26/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF4B | 10.6.33.27/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF5A | 10.6.33.28/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF5B | 10.6.33.29/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF6A | 10.6.33.30/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF6B | 10.6.33.31/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF7A | 10.6.33.32/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF7B | 10.6.33.33/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF8A | 10.6.33.34/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF8B | 10.6.33.35/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF9A | 10.6.33.36/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF9B | 10.6.33.37/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF10A | 10.6.33.38/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF10B | 10.6.33.39/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF11A | 10.6.33.40/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF11B | 10.6.33.41/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF12A | 10.6.33.42/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF12B | 10.6.33.43/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF13A | 10.6.33.44/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF13B | 10.6.33.45/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF14A | 10.6.33.46/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF14B | 10.6.33.47/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE1 | 10.6.33.10/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE2 | 10.6.33.11/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE3 | 10.6.33.12/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE4 | 10.6.33.13/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF1A | 10.6.35.20/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF1B | 10.6.35.21/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF2A | 10.6.35.22/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF2B | 10.6.35.23/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF3A | 10.6.35.24/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF3B | 10.6.35.25/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF4A | 10.6.35.26/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF4B | 10.6.35.27/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF5A | 10.6.35.28/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF5B | 10.6.35.29/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF6A | 10.6.35.30/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF6B | 10.6.35.31/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF7A | 10.6.35.32/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF7B | 10.6.35.33/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF8A | 10.6.35.34/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF8B | 10.6.35.35/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF9A | 10.6.35.36/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF9B | 10.6.35.37/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF10A | 10.6.35.38/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF10B | 10.6.35.39/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF11A | 10.6.35.40/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF11B | 10.6.35.41/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF12A | 10.6.35.42/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF12B | 10.6.35.43/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF13A | 10.6.35.44/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF13B | 10.6.35.45/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF14A | 10.6.35.46/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF14B | 10.6.35.47/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE1 | 10.6.65.10/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE2 | 10.6.65.11/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE3 | 10.6.65.12/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE4 | 10.6.65.13/24 | vEOS-LAB | Provisioned |
| AMS | super-spine | SUPER-SPINE1 | 10.6.0.10/24 | 7060 | Provisioned |
| AMS | super-spine | SUPER-SPINE2 | 10.6.0.11/24 | 7280R | Provisioned |
| AMS | super-spine | SUPER-SPINE3 | 10.6.0.12/24 | 7280R | Provisioned |
| AMS | super-spine | SUPER-SPINE4 | 10.6.0.13/24 | 7280R | Provisioned |
| AMS | super-spine | SUPER-SPINE5 | 10.6.0.14/24 | 7280R | Provisioned |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | DC1-POD1-LEAF1A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF1B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF1B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet1/1 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet1/1 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet1/1 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet1/1 |
| l3leaf | DC1-POD1-LEAF1B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet2/1 |
| l3leaf | DC1-POD1-LEAF1B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet2/1 |
| l3leaf | DC1-POD1-LEAF1B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet2/1 |
| l3leaf | DC1-POD1-LEAF1B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet2/1 |
| l3leaf | DC1-POD1-LEAF2A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF2B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF2A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF2B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF2A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet3/1 |
| l3leaf | DC1-POD1-LEAF2A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet3/1 |
| l3leaf | DC1-POD1-LEAF2A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet3/1 |
| l3leaf | DC1-POD1-LEAF2A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet3/1 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet4/1 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet4/1 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet4/1 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet4/1 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF3B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF3B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet5/1 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet5/1 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet5/1 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet5/1 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet6/1 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet6/1 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet6/1 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet6/1 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF4B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF4B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet7/1 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet7/1 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet7/1 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet7/1 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet8/1 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet8/1 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet8/1 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet8/1 |
| l3leaf | DC1-POD1-LEAF5A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF5B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF5A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF5B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF5A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet9/1 |
| l3leaf | DC1-POD1-LEAF5A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet9/1 |
| l3leaf | DC1-POD1-LEAF5A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet9/1 |
| l3leaf | DC1-POD1-LEAF5A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet9/1 |
| l3leaf | DC1-POD1-LEAF5B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet10/1 |
| l3leaf | DC1-POD1-LEAF5B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet10/1 |
| l3leaf | DC1-POD1-LEAF5B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet10/1 |
| l3leaf | DC1-POD1-LEAF5B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet10/1 |
| l3leaf | DC1-POD1-LEAF6A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF6B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF6A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF6B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF6A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet11/1 |
| l3leaf | DC1-POD1-LEAF6A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet11/1 |
| l3leaf | DC1-POD1-LEAF6A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet11/1 |
| l3leaf | DC1-POD1-LEAF6A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet11/1 |
| l3leaf | DC1-POD1-LEAF6B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet12/1 |
| l3leaf | DC1-POD1-LEAF6B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet12/1 |
| l3leaf | DC1-POD1-LEAF6B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet12/1 |
| l3leaf | DC1-POD1-LEAF6B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet12/1 |
| l3leaf | DC1-POD1-LEAF7A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF7B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF7A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF7B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF7A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet13/1 |
| l3leaf | DC1-POD1-LEAF7A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet13/1 |
| l3leaf | DC1-POD1-LEAF7A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet13/1 |
| l3leaf | DC1-POD1-LEAF7A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet13/1 |
| l3leaf | DC1-POD1-LEAF7B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet14/1 |
| l3leaf | DC1-POD1-LEAF7B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet14/1 |
| l3leaf | DC1-POD1-LEAF7B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet14/1 |
| l3leaf | DC1-POD1-LEAF7B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet14/1 |
| l3leaf | DC1-POD1-LEAF8A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF8B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF8A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF8B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF8A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF8A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF8A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF8A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF8B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF8B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF8B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF8B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF9A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF9B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF9A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF9B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF9A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet17/1 |
| l3leaf | DC1-POD1-LEAF9A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet17/1 |
| l3leaf | DC1-POD1-LEAF9A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet17/1 |
| l3leaf | DC1-POD1-LEAF9A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet17/1 |
| l3leaf | DC1-POD1-LEAF9B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet18/1 |
| l3leaf | DC1-POD1-LEAF9B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet18/1 |
| l3leaf | DC1-POD1-LEAF9B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet18/1 |
| l3leaf | DC1-POD1-LEAF9B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet18/1 |
| l3leaf | DC1-POD1-LEAF10A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF10B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF10A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF10B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF10A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet19/1 |
| l3leaf | DC1-POD1-LEAF10A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet19/1 |
| l3leaf | DC1-POD1-LEAF10A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet19/1 |
| l3leaf | DC1-POD1-LEAF10A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet19/1 |
| l3leaf | DC1-POD1-LEAF10B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet20/1 |
| l3leaf | DC1-POD1-LEAF10B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet20/1 |
| l3leaf | DC1-POD1-LEAF10B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet20/1 |
| l3leaf | DC1-POD1-LEAF10B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet20/1 |
| l3leaf | DC1-POD1-LEAF11A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF11B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF11A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF11B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF11A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet21/1 |
| l3leaf | DC1-POD1-LEAF11A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet21/1 |
| l3leaf | DC1-POD1-LEAF11A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet21/1 |
| l3leaf | DC1-POD1-LEAF11A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet21/1 |
| l3leaf | DC1-POD1-LEAF11B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet22/1 |
| l3leaf | DC1-POD1-LEAF11B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet22/1 |
| l3leaf | DC1-POD1-LEAF11B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet22/1 |
| l3leaf | DC1-POD1-LEAF11B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet22/1 |
| l3leaf | DC1-POD1-LEAF12A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF12B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF12A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF12B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF12A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet23/1 |
| l3leaf | DC1-POD1-LEAF12A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet23/1 |
| l3leaf | DC1-POD1-LEAF12A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet23/1 |
| l3leaf | DC1-POD1-LEAF12A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet23/1 |
| l3leaf | DC1-POD1-LEAF12B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet24/1 |
| l3leaf | DC1-POD1-LEAF12B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet24/1 |
| l3leaf | DC1-POD1-LEAF12B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet24/1 |
| l3leaf | DC1-POD1-LEAF12B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet24/1 |
| l3leaf | DC1-POD1-LEAF13A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF13B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF13A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF13B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF13A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet25/1 |
| l3leaf | DC1-POD1-LEAF13A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet25/1 |
| l3leaf | DC1-POD1-LEAF13A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet25/1 |
| l3leaf | DC1-POD1-LEAF13A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet25/1 |
| l3leaf | DC1-POD1-LEAF13B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet26/1 |
| l3leaf | DC1-POD1-LEAF13B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet26/1 |
| l3leaf | DC1-POD1-LEAF13B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet26/1 |
| l3leaf | DC1-POD1-LEAF13B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet26/1 |
| l3leaf | DC1-POD1-LEAF14A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF14B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF14A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF14B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF14A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet27/1 |
| l3leaf | DC1-POD1-LEAF14A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet27/1 |
| l3leaf | DC1-POD1-LEAF14A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet27/1 |
| l3leaf | DC1-POD1-LEAF14A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet27/1 |
| l3leaf | DC1-POD1-LEAF14B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet28/1 |
| l3leaf | DC1-POD1-LEAF14B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet28/1 |
| l3leaf | DC1-POD1-LEAF14B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet28/1 |
| l3leaf | DC1-POD1-LEAF14B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet28/1 |
| spine | DC1-POD1-SPINE1 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet1/1 |
| spine | DC1-POD1-SPINE1 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet1/1 |
| spine | DC1-POD1-SPINE1 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet1/1 |
| spine | DC1-POD1-SPINE1 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet1/1 |
| spine | DC1-POD1-SPINE2 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet2/1 |
| spine | DC1-POD1-SPINE2 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet2/1 |
| spine | DC1-POD1-SPINE2 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet2/1 |
| spine | DC1-POD1-SPINE2 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet2/1 |
| spine | DC1-POD1-SPINE3 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet3/1 |
| spine | DC1-POD1-SPINE3 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet3/1 |
| spine | DC1-POD1-SPINE3 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet3/1 |
| spine | DC1-POD1-SPINE3 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet3/1 |
| spine | DC1-POD1-SPINE4 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet4/1 |
| spine | DC1-POD1-SPINE4 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet4/1 |
| spine | DC1-POD1-SPINE4 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet4/1 |
| spine | DC1-POD1-SPINE4 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet4/1 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF1B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF1B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet1/1 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet1/1 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet1/1 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet1/1 |
| l3leaf | DC1-POD2-LEAF1B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet2/1 |
| l3leaf | DC1-POD2-LEAF1B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet2/1 |
| l3leaf | DC1-POD2-LEAF1B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet2/1 |
| l3leaf | DC1-POD2-LEAF1B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet2/1 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF2B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF2B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet3/1 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet3/1 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet3/1 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet3/1 |
| l3leaf | DC1-POD2-LEAF2B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet4/1 |
| l3leaf | DC1-POD2-LEAF2B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet4/1 |
| l3leaf | DC1-POD2-LEAF2B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet4/1 |
| l3leaf | DC1-POD2-LEAF2B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet4/1 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF3B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF3B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet5/1 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet5/1 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet5/1 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet5/1 |
| l3leaf | DC1-POD2-LEAF3B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet6/1 |
| l3leaf | DC1-POD2-LEAF3B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet6/1 |
| l3leaf | DC1-POD2-LEAF3B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet6/1 |
| l3leaf | DC1-POD2-LEAF3B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet6/1 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF4B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF4B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet7/1 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet7/1 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet7/1 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet7/1 |
| l3leaf | DC1-POD2-LEAF4B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet8/1 |
| l3leaf | DC1-POD2-LEAF4B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet8/1 |
| l3leaf | DC1-POD2-LEAF4B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet8/1 |
| l3leaf | DC1-POD2-LEAF4B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet8/1 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF5B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF5B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet9/1 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet9/1 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet9/1 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet9/1 |
| l3leaf | DC1-POD2-LEAF5B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet10/1 |
| l3leaf | DC1-POD2-LEAF5B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet10/1 |
| l3leaf | DC1-POD2-LEAF5B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet10/1 |
| l3leaf | DC1-POD2-LEAF5B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet10/1 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF6B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF6B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet11/1 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet11/1 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet11/1 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet11/1 |
| l3leaf | DC1-POD2-LEAF6B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet12/1 |
| l3leaf | DC1-POD2-LEAF6B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet12/1 |
| l3leaf | DC1-POD2-LEAF6B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet12/1 |
| l3leaf | DC1-POD2-LEAF6B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet12/1 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF7B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF7B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet13/1 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet13/1 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet13/1 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet13/1 |
| l3leaf | DC1-POD2-LEAF7B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet14/1 |
| l3leaf | DC1-POD2-LEAF7B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet14/1 |
| l3leaf | DC1-POD2-LEAF7B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet14/1 |
| l3leaf | DC1-POD2-LEAF7B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet14/1 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF8B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF8B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF8B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF8B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF8B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF8B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF9B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF9B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet17/1 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet17/1 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet17/1 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet17/1 |
| l3leaf | DC1-POD2-LEAF9B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet18/1 |
| l3leaf | DC1-POD2-LEAF9B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet18/1 |
| l3leaf | DC1-POD2-LEAF9B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet18/1 |
| l3leaf | DC1-POD2-LEAF9B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet18/1 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF10B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF10B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet19/1 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet19/1 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet19/1 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet19/1 |
| l3leaf | DC1-POD2-LEAF10B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet20/1 |
| l3leaf | DC1-POD2-LEAF10B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet20/1 |
| l3leaf | DC1-POD2-LEAF10B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet20/1 |
| l3leaf | DC1-POD2-LEAF10B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet20/1 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF11B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF11B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet21/1 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet21/1 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet21/1 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet21/1 |
| l3leaf | DC1-POD2-LEAF11B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet22/1 |
| l3leaf | DC1-POD2-LEAF11B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet22/1 |
| l3leaf | DC1-POD2-LEAF11B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet22/1 |
| l3leaf | DC1-POD2-LEAF11B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet22/1 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF12B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF12B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet23/1 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet23/1 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet23/1 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet23/1 |
| l3leaf | DC1-POD2-LEAF12B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet24/1 |
| l3leaf | DC1-POD2-LEAF12B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet24/1 |
| l3leaf | DC1-POD2-LEAF12B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet24/1 |
| l3leaf | DC1-POD2-LEAF12B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet24/1 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF13B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF13B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet25/1 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet25/1 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet25/1 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet25/1 |
| l3leaf | DC1-POD2-LEAF13B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet26/1 |
| l3leaf | DC1-POD2-LEAF13B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet26/1 |
| l3leaf | DC1-POD2-LEAF13B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet26/1 |
| l3leaf | DC1-POD2-LEAF13B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet26/1 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF14B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF14B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet27/1 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet27/1 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet27/1 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet27/1 |
| l3leaf | DC1-POD2-LEAF14B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet28/1 |
| l3leaf | DC1-POD2-LEAF14B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet28/1 |
| l3leaf | DC1-POD2-LEAF14B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet28/1 |
| l3leaf | DC1-POD2-LEAF14B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet28/1 |
| spine | DC1-POD2-SPINE1 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet5/1 |
| spine | DC1-POD2-SPINE1 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet5/1 |
| spine | DC1-POD2-SPINE1 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet5/1 |
| spine | DC1-POD2-SPINE1 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet5/2 |
| spine | DC1-POD2-SPINE2 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet6/1 |
| spine | DC1-POD2-SPINE2 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet6/1 |
| spine | DC1-POD2-SPINE2 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet6/1 |
| spine | DC1-POD2-SPINE2 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet6/1 |
| spine | DC1-POD2-SPINE3 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet7/1 |
| spine | DC1-POD2-SPINE3 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet7/1 |
| spine | DC1-POD2-SPINE3 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet7/1 |
| spine | DC1-POD2-SPINE3 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet7/1 |
| spine | DC1-POD2-SPINE4 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet8/1 |
| spine | DC1-POD2-SPINE4 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet8/1 |
| spine | DC1-POD2-SPINE4 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet8/1 |
| spine | DC1-POD2-SPINE4 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet8/1 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF1B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF1B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet1/1 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet1/1 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet1/1 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet1/1 |
| l3leaf | DC2-POD1-LEAF1B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet2/1 |
| l3leaf | DC2-POD1-LEAF1B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet2/1 |
| l3leaf | DC2-POD1-LEAF1B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet2/1 |
| l3leaf | DC2-POD1-LEAF1B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet2/1 |
| l3leaf | DC2-POD1-LEAF2A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF2B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF2A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF2B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF2A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet3/1 |
| l3leaf | DC2-POD1-LEAF2A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet3/1 |
| l3leaf | DC2-POD1-LEAF2A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet3/1 |
| l3leaf | DC2-POD1-LEAF2A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet3/1 |
| l3leaf | DC2-POD1-LEAF2B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet4/1 |
| l3leaf | DC2-POD1-LEAF2B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet4/1 |
| l3leaf | DC2-POD1-LEAF2B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet4/1 |
| l3leaf | DC2-POD1-LEAF2B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet4/1 |
| l3leaf | DC2-POD1-LEAF3A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF3B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF3A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF3B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF3A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet5/1 |
| l3leaf | DC2-POD1-LEAF3A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet5/1 |
| l3leaf | DC2-POD1-LEAF3A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet5/1 |
| l3leaf | DC2-POD1-LEAF3A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet5/1 |
| l3leaf | DC2-POD1-LEAF3B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet6/1 |
| l3leaf | DC2-POD1-LEAF3B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet6/1 |
| l3leaf | DC2-POD1-LEAF3B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet6/1 |
| l3leaf | DC2-POD1-LEAF3B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet6/1 |
| l3leaf | DC2-POD1-LEAF4A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF4B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF4A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF4B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF4A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet7/1 |
| l3leaf | DC2-POD1-LEAF4A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet7/1 |
| l3leaf | DC2-POD1-LEAF4A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet7/1 |
| l3leaf | DC2-POD1-LEAF4A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet7/1 |
| l3leaf | DC2-POD1-LEAF4B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet8/1 |
| l3leaf | DC2-POD1-LEAF4B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet8/1 |
| l3leaf | DC2-POD1-LEAF4B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet8/1 |
| l3leaf | DC2-POD1-LEAF4B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet8/1 |
| l3leaf | DC2-POD1-LEAF5A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF5B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF5A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF5B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF5A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet9/1 |
| l3leaf | DC2-POD1-LEAF5A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet9/1 |
| l3leaf | DC2-POD1-LEAF5A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet9/1 |
| l3leaf | DC2-POD1-LEAF5A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet9/1 |
| l3leaf | DC2-POD1-LEAF5B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet10/1 |
| l3leaf | DC2-POD1-LEAF5B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet10/1 |
| l3leaf | DC2-POD1-LEAF5B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet10/1 |
| l3leaf | DC2-POD1-LEAF5B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet10/1 |
| l3leaf | DC2-POD1-LEAF6A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF6B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF6A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF6B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF6A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet11/1 |
| l3leaf | DC2-POD1-LEAF6A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet11/1 |
| l3leaf | DC2-POD1-LEAF6A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet11/1 |
| l3leaf | DC2-POD1-LEAF6A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet11/1 |
| l3leaf | DC2-POD1-LEAF6B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet12/1 |
| l3leaf | DC2-POD1-LEAF6B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet12/1 |
| l3leaf | DC2-POD1-LEAF6B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet12/1 |
| l3leaf | DC2-POD1-LEAF6B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet12/1 |
| l3leaf | DC2-POD1-LEAF7A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF7B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF7A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF7B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF7A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet13/1 |
| l3leaf | DC2-POD1-LEAF7A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet13/1 |
| l3leaf | DC2-POD1-LEAF7A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet13/1 |
| l3leaf | DC2-POD1-LEAF7A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet13/1 |
| l3leaf | DC2-POD1-LEAF7B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet14/1 |
| l3leaf | DC2-POD1-LEAF7B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet14/1 |
| l3leaf | DC2-POD1-LEAF7B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet14/1 |
| l3leaf | DC2-POD1-LEAF7B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet14/1 |
| l3leaf | DC2-POD1-LEAF8A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF8B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF8A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF8B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF8A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF8A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF8A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF8A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF8B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF8B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF8B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF8B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF9A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF9B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF9A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF9B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF9A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet17/1 |
| l3leaf | DC2-POD1-LEAF9A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet17/1 |
| l3leaf | DC2-POD1-LEAF9A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet17/1 |
| l3leaf | DC2-POD1-LEAF9A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet17/1 |
| l3leaf | DC2-POD1-LEAF9B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet18/1 |
| l3leaf | DC2-POD1-LEAF9B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet18/1 |
| l3leaf | DC2-POD1-LEAF9B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet18/1 |
| l3leaf | DC2-POD1-LEAF9B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet18/1 |
| l3leaf | DC2-POD1-LEAF10A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF10B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF10A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF10B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF10A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet19/1 |
| l3leaf | DC2-POD1-LEAF10A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet19/1 |
| l3leaf | DC2-POD1-LEAF10A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet19/1 |
| l3leaf | DC2-POD1-LEAF10A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet19/1 |
| l3leaf | DC2-POD1-LEAF10B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet20/1 |
| l3leaf | DC2-POD1-LEAF10B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet20/1 |
| l3leaf | DC2-POD1-LEAF10B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet20/1 |
| l3leaf | DC2-POD1-LEAF10B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet20/1 |
| l3leaf | DC2-POD1-LEAF11A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF11B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF11A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF11B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF11A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet21/1 |
| l3leaf | DC2-POD1-LEAF11A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet21/1 |
| l3leaf | DC2-POD1-LEAF11A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet21/1 |
| l3leaf | DC2-POD1-LEAF11A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet21/1 |
| l3leaf | DC2-POD1-LEAF11B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet22/1 |
| l3leaf | DC2-POD1-LEAF11B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet22/1 |
| l3leaf | DC2-POD1-LEAF11B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet22/1 |
| l3leaf | DC2-POD1-LEAF11B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet22/1 |
| l3leaf | DC2-POD1-LEAF12A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF12B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF12A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF12B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF12A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet23/1 |
| l3leaf | DC2-POD1-LEAF12A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet23/1 |
| l3leaf | DC2-POD1-LEAF12A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet23/1 |
| l3leaf | DC2-POD1-LEAF12A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet23/1 |
| l3leaf | DC2-POD1-LEAF12B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet24/1 |
| l3leaf | DC2-POD1-LEAF12B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet24/1 |
| l3leaf | DC2-POD1-LEAF12B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet24/1 |
| l3leaf | DC2-POD1-LEAF12B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet24/1 |
| l3leaf | DC2-POD1-LEAF13A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF13B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF13A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF13B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF13A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet25/1 |
| l3leaf | DC2-POD1-LEAF13A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet25/1 |
| l3leaf | DC2-POD1-LEAF13A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet25/1 |
| l3leaf | DC2-POD1-LEAF13A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet25/1 |
| l3leaf | DC2-POD1-LEAF13B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet26/1 |
| l3leaf | DC2-POD1-LEAF13B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet26/1 |
| l3leaf | DC2-POD1-LEAF13B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet26/1 |
| l3leaf | DC2-POD1-LEAF13B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet26/1 |
| l3leaf | DC2-POD1-LEAF14A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF14B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF14A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF14B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF14A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet27/1 |
| l3leaf | DC2-POD1-LEAF14A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet27/1 |
| l3leaf | DC2-POD1-LEAF14A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet27/1 |
| l3leaf | DC2-POD1-LEAF14A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet27/1 |
| l3leaf | DC2-POD1-LEAF14B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet28/1 |
| l3leaf | DC2-POD1-LEAF14B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet28/1 |
| l3leaf | DC2-POD1-LEAF14B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet28/1 |
| l3leaf | DC2-POD1-LEAF14B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet28/1 |
| spine | DC2-POD1-SPINE1 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet9/1 |
| spine | DC2-POD1-SPINE1 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet9/1 |
| spine | DC2-POD1-SPINE1 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet9/1 |
| spine | DC2-POD1-SPINE1 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet9/1 |
| spine | DC2-POD1-SPINE2 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet10/1 |
| spine | DC2-POD1-SPINE2 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet10/1 |
| spine | DC2-POD1-SPINE2 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet10/1 |
| spine | DC2-POD1-SPINE2 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet10/1 |
| spine | DC2-POD1-SPINE3 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet11/1 |
| spine | DC2-POD1-SPINE3 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet11/1 |
| spine | DC2-POD1-SPINE3 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet11/1 |
| spine | DC2-POD1-SPINE3 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet11/1 |
| spine | DC2-POD1-SPINE4 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet12/1 |
| spine | DC2-POD1-SPINE4 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet12/1 |
| spine | DC2-POD1-SPINE4 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet12/1 |
| spine | DC2-POD1-SPINE4 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet12/1 |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 172.16.0.0/24 | 256 | 32 | 12.5 % |
| 172.16.32.0/24 | 256 | 32 | 12.5 % |
| 172.16.64.0/24 | 256 | 32 | 12.5 % |
| 172.17.0.0/24 | 256 | 104 | 40.63 % |
| 172.17.32.0/24 | 256 | 104 | 40.63 % |
| 172.17.64.0/24 | 256 | 96 | 37.5 % |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| DC1-POD1-LEAF1A | Ethernet29/1 | 172.17.0.153/31 | DC1-POD1-SPINE1 | Ethernet1/1 | 172.17.0.152/31 |
| DC1-POD1-LEAF1A | Ethernet30/1 | 172.17.0.155/31 | DC1-POD1-SPINE2 | Ethernet1/1 | 172.17.0.154/31 |
| DC1-POD1-LEAF1A | Ethernet31/1 | 172.17.0.157/31 | DC1-POD1-SPINE3 | Ethernet1/1 | 172.17.0.156/31 |
| DC1-POD1-LEAF1A | Ethernet32/1 | 172.17.0.159/31 | DC1-POD1-SPINE4 | Ethernet1/1 | 172.17.0.158/31 |
| DC1-POD1-LEAF1B | Ethernet29/1 | 172.17.0.161/31 | DC1-POD1-SPINE1 | Ethernet2/1 | 172.17.0.160/31 |
| DC1-POD1-LEAF1B | Ethernet30/1 | 172.17.0.163/31 | DC1-POD1-SPINE2 | Ethernet2/1 | 172.17.0.162/31 |
| DC1-POD1-LEAF1B | Ethernet31/1 | 172.17.0.165/31 | DC1-POD1-SPINE3 | Ethernet2/1 | 172.17.0.164/31 |
| DC1-POD1-LEAF1B | Ethernet32/1 | 172.17.0.167/31 | DC1-POD1-SPINE4 | Ethernet2/1 | 172.17.0.166/31 |
| DC1-POD1-LEAF2A | Ethernet29/1 | 172.17.0.169/31 | DC1-POD1-SPINE1 | Ethernet3/1 | 172.17.0.168/31 |
| DC1-POD1-LEAF2A | Ethernet30/1 | 172.17.0.171/31 | DC1-POD1-SPINE2 | Ethernet3/1 | 172.17.0.170/31 |
| DC1-POD1-LEAF2A | Ethernet31/1 | 172.17.0.173/31 | DC1-POD1-SPINE3 | Ethernet3/1 | 172.17.0.172/31 |
| DC1-POD1-LEAF2A | Ethernet32/1 | 172.17.0.175/31 | DC1-POD1-SPINE4 | Ethernet3/1 | 172.17.0.174/31 |
| DC1-POD1-LEAF2B | Ethernet29/1 | 172.17.0.177/31 | DC1-POD1-SPINE1 | Ethernet4/1 | 172.17.0.176/31 |
| DC1-POD1-LEAF2B | Ethernet30/1 | 172.17.0.179/31 | DC1-POD1-SPINE2 | Ethernet4/1 | 172.17.0.178/31 |
| DC1-POD1-LEAF2B | Ethernet31/1 | 172.17.0.181/31 | DC1-POD1-SPINE3 | Ethernet4/1 | 172.17.0.180/31 |
| DC1-POD1-LEAF2B | Ethernet32/1 | 172.17.0.183/31 | DC1-POD1-SPINE4 | Ethernet4/1 | 172.17.0.182/31 |
| DC1-POD1-LEAF3A | Ethernet29/1 | 172.17.0.185/31 | DC1-POD1-SPINE1 | Ethernet5/1 | 172.17.0.184/31 |
| DC1-POD1-LEAF3A | Ethernet30/1 | 172.17.0.187/31 | DC1-POD1-SPINE2 | Ethernet5/1 | 172.17.0.186/31 |
| DC1-POD1-LEAF3A | Ethernet31/1 | 172.17.0.189/31 | DC1-POD1-SPINE3 | Ethernet5/1 | 172.17.0.188/31 |
| DC1-POD1-LEAF3A | Ethernet32/1 | 172.17.0.191/31 | DC1-POD1-SPINE4 | Ethernet5/1 | 172.17.0.190/31 |
| DC1-POD1-LEAF3B | Ethernet29/1 | 172.17.0.193/31 | DC1-POD1-SPINE1 | Ethernet6/1 | 172.17.0.192/31 |
| DC1-POD1-LEAF3B | Ethernet30/1 | 172.17.0.195/31 | DC1-POD1-SPINE2 | Ethernet6/1 | 172.17.0.194/31 |
| DC1-POD1-LEAF3B | Ethernet31/1 | 172.17.0.197/31 | DC1-POD1-SPINE3 | Ethernet6/1 | 172.17.0.196/31 |
| DC1-POD1-LEAF3B | Ethernet32/1 | 172.17.0.199/31 | DC1-POD1-SPINE4 | Ethernet6/1 | 172.17.0.198/31 |
| DC1-POD1-LEAF4A | Ethernet29/1 | 172.17.0.201/31 | DC1-POD1-SPINE1 | Ethernet7/1 | 172.17.0.200/31 |
| DC1-POD1-LEAF4A | Ethernet30/1 | 172.17.0.203/31 | DC1-POD1-SPINE2 | Ethernet7/1 | 172.17.0.202/31 |
| DC1-POD1-LEAF4A | Ethernet31/1 | 172.17.0.205/31 | DC1-POD1-SPINE3 | Ethernet7/1 | 172.17.0.204/31 |
| DC1-POD1-LEAF4A | Ethernet32/1 | 172.17.0.207/31 | DC1-POD1-SPINE4 | Ethernet7/1 | 172.17.0.206/31 |
| DC1-POD1-LEAF4B | Ethernet29/1 | 172.17.0.209/31 | DC1-POD1-SPINE1 | Ethernet8/1 | 172.17.0.208/31 |
| DC1-POD1-LEAF4B | Ethernet30/1 | 172.17.0.211/31 | DC1-POD1-SPINE2 | Ethernet8/1 | 172.17.0.210/31 |
| DC1-POD1-LEAF4B | Ethernet31/1 | 172.17.0.213/31 | DC1-POD1-SPINE3 | Ethernet8/1 | 172.17.0.212/31 |
| DC1-POD1-LEAF4B | Ethernet32/1 | 172.17.0.215/31 | DC1-POD1-SPINE4 | Ethernet8/1 | 172.17.0.214/31 |
| DC1-POD1-LEAF5A | Ethernet29/1 | 172.17.0.217/31 | DC1-POD1-SPINE1 | Ethernet9/1 | 172.17.0.216/31 |
| DC1-POD1-LEAF5A | Ethernet30/1 | 172.17.0.219/31 | DC1-POD1-SPINE2 | Ethernet9/1 | 172.17.0.218/31 |
| DC1-POD1-LEAF5A | Ethernet31/1 | 172.17.0.221/31 | DC1-POD1-SPINE3 | Ethernet9/1 | 172.17.0.220/31 |
| DC1-POD1-LEAF5A | Ethernet32/1 | 172.17.0.223/31 | DC1-POD1-SPINE4 | Ethernet9/1 | 172.17.0.222/31 |
| DC1-POD1-LEAF5B | Ethernet29/1 | 172.17.0.225/31 | DC1-POD1-SPINE1 | Ethernet10/1 | 172.17.0.224/31 |
| DC1-POD1-LEAF5B | Ethernet30/1 | 172.17.0.227/31 | DC1-POD1-SPINE2 | Ethernet10/1 | 172.17.0.226/31 |
| DC1-POD1-LEAF5B | Ethernet31/1 | 172.17.0.229/31 | DC1-POD1-SPINE3 | Ethernet10/1 | 172.17.0.228/31 |
| DC1-POD1-LEAF5B | Ethernet32/1 | 172.17.0.231/31 | DC1-POD1-SPINE4 | Ethernet10/1 | 172.17.0.230/31 |
| DC1-POD1-LEAF6A | Ethernet29/1 | 172.17.0.233/31 | DC1-POD1-SPINE1 | Ethernet11/1 | 172.17.0.232/31 |
| DC1-POD1-LEAF6A | Ethernet30/1 | 172.17.0.235/31 | DC1-POD1-SPINE2 | Ethernet11/1 | 172.17.0.234/31 |
| DC1-POD1-LEAF6A | Ethernet31/1 | 172.17.0.237/31 | DC1-POD1-SPINE3 | Ethernet11/1 | 172.17.0.236/31 |
| DC1-POD1-LEAF6A | Ethernet32/1 | 172.17.0.239/31 | DC1-POD1-SPINE4 | Ethernet11/1 | 172.17.0.238/31 |
| DC1-POD1-LEAF6B | Ethernet29/1 | 172.17.0.241/31 | DC1-POD1-SPINE1 | Ethernet12/1 | 172.17.0.240/31 |
| DC1-POD1-LEAF6B | Ethernet30/1 | 172.17.0.243/31 | DC1-POD1-SPINE2 | Ethernet12/1 | 172.17.0.242/31 |
| DC1-POD1-LEAF6B | Ethernet31/1 | 172.17.0.245/31 | DC1-POD1-SPINE3 | Ethernet12/1 | 172.17.0.244/31 |
| DC1-POD1-LEAF6B | Ethernet32/1 | 172.17.0.247/31 | DC1-POD1-SPINE4 | Ethernet12/1 | 172.17.0.246/31 |
| DC1-POD1-LEAF7A | Ethernet29/1 | 172.17.0.249/31 | DC1-POD1-SPINE1 | Ethernet13/1 | 172.17.0.248/31 |
| DC1-POD1-LEAF7A | Ethernet30/1 | 172.17.0.251/31 | DC1-POD1-SPINE2 | Ethernet13/1 | 172.17.0.250/31 |
| DC1-POD1-LEAF7A | Ethernet31/1 | 172.17.0.253/31 | DC1-POD1-SPINE3 | Ethernet13/1 | 172.17.0.252/31 |
| DC1-POD1-LEAF7A | Ethernet32/1 | 172.17.0.255/31 | DC1-POD1-SPINE4 | Ethernet13/1 | 172.17.0.254/31 |
| DC1-POD1-LEAF7B | Ethernet29/1 | 172.17.1.1/31 | DC1-POD1-SPINE1 | Ethernet14/1 | 172.17.1.0/31 |
| DC1-POD1-LEAF7B | Ethernet30/1 | 172.17.1.3/31 | DC1-POD1-SPINE2 | Ethernet14/1 | 172.17.1.2/31 |
| DC1-POD1-LEAF7B | Ethernet31/1 | 172.17.1.5/31 | DC1-POD1-SPINE3 | Ethernet14/1 | 172.17.1.4/31 |
| DC1-POD1-LEAF7B | Ethernet32/1 | 172.17.1.7/31 | DC1-POD1-SPINE4 | Ethernet14/1 | 172.17.1.6/31 |
| DC1-POD1-LEAF8A | Ethernet29/1 | 172.17.1.9/31 | DC1-POD1-SPINE1 | Ethernet15/1 | 172.17.1.8/31 |
| DC1-POD1-LEAF8A | Ethernet30/1 | 172.17.1.11/31 | DC1-POD1-SPINE2 | Ethernet15/1 | 172.17.1.10/31 |
| DC1-POD1-LEAF8A | Ethernet31/1 | 172.17.1.13/31 | DC1-POD1-SPINE3 | Ethernet15/1 | 172.17.1.12/31 |
| DC1-POD1-LEAF8A | Ethernet32/1 | 172.17.1.15/31 | DC1-POD1-SPINE4 | Ethernet15/1 | 172.17.1.14/31 |
| DC1-POD1-LEAF8B | Ethernet29/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet16/1 | 172.17.1.16/31 |
| DC1-POD1-LEAF8B | Ethernet30/1 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet16/1 | 172.17.1.18/31 |
| DC1-POD1-LEAF8B | Ethernet31/1 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet16/1 | 172.17.1.20/31 |
| DC1-POD1-LEAF8B | Ethernet32/1 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet16/1 | 172.17.1.22/31 |
| DC1-POD1-LEAF9A | Ethernet29/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet17/1 | 172.17.1.24/31 |
| DC1-POD1-LEAF9A | Ethernet30/1 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet17/1 | 172.17.1.26/31 |
| DC1-POD1-LEAF9A | Ethernet31/1 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet17/1 | 172.17.1.28/31 |
| DC1-POD1-LEAF9A | Ethernet32/1 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet17/1 | 172.17.1.30/31 |
| DC1-POD1-LEAF9B | Ethernet29/1 | 172.17.1.33/31 | DC1-POD1-SPINE1 | Ethernet18/1 | 172.17.1.32/31 |
| DC1-POD1-LEAF9B | Ethernet30/1 | 172.17.1.35/31 | DC1-POD1-SPINE2 | Ethernet18/1 | 172.17.1.34/31 |
| DC1-POD1-LEAF9B | Ethernet31/1 | 172.17.1.37/31 | DC1-POD1-SPINE3 | Ethernet18/1 | 172.17.1.36/31 |
| DC1-POD1-LEAF9B | Ethernet32/1 | 172.17.1.39/31 | DC1-POD1-SPINE4 | Ethernet18/1 | 172.17.1.38/31 |
| DC1-POD1-LEAF10A | Ethernet29/1 | 172.17.1.41/31 | DC1-POD1-SPINE1 | Ethernet19/1 | 172.17.1.40/31 |
| DC1-POD1-LEAF10A | Ethernet30/1 | 172.17.1.43/31 | DC1-POD1-SPINE2 | Ethernet19/1 | 172.17.1.42/31 |
| DC1-POD1-LEAF10A | Ethernet31/1 | 172.17.1.45/31 | DC1-POD1-SPINE3 | Ethernet19/1 | 172.17.1.44/31 |
| DC1-POD1-LEAF10A | Ethernet32/1 | 172.17.1.47/31 | DC1-POD1-SPINE4 | Ethernet19/1 | 172.17.1.46/31 |
| DC1-POD1-LEAF10B | Ethernet29/1 | 172.17.1.49/31 | DC1-POD1-SPINE1 | Ethernet20/1 | 172.17.1.48/31 |
| DC1-POD1-LEAF10B | Ethernet30/1 | 172.17.1.51/31 | DC1-POD1-SPINE2 | Ethernet20/1 | 172.17.1.50/31 |
| DC1-POD1-LEAF10B | Ethernet31/1 | 172.17.1.53/31 | DC1-POD1-SPINE3 | Ethernet20/1 | 172.17.1.52/31 |
| DC1-POD1-LEAF10B | Ethernet32/1 | 172.17.1.55/31 | DC1-POD1-SPINE4 | Ethernet20/1 | 172.17.1.54/31 |
| DC1-POD1-LEAF11A | Ethernet29/1 | 172.17.1.57/31 | DC1-POD1-SPINE1 | Ethernet21/1 | 172.17.1.56/31 |
| DC1-POD1-LEAF11A | Ethernet30/1 | 172.17.1.59/31 | DC1-POD1-SPINE2 | Ethernet21/1 | 172.17.1.58/31 |
| DC1-POD1-LEAF11A | Ethernet31/1 | 172.17.1.61/31 | DC1-POD1-SPINE3 | Ethernet21/1 | 172.17.1.60/31 |
| DC1-POD1-LEAF11A | Ethernet32/1 | 172.17.1.63/31 | DC1-POD1-SPINE4 | Ethernet21/1 | 172.17.1.62/31 |
| DC1-POD1-LEAF11B | Ethernet29/1 | 172.17.1.65/31 | DC1-POD1-SPINE1 | Ethernet22/1 | 172.17.1.64/31 |
| DC1-POD1-LEAF11B | Ethernet30/1 | 172.17.1.67/31 | DC1-POD1-SPINE2 | Ethernet22/1 | 172.17.1.66/31 |
| DC1-POD1-LEAF11B | Ethernet31/1 | 172.17.1.69/31 | DC1-POD1-SPINE3 | Ethernet22/1 | 172.17.1.68/31 |
| DC1-POD1-LEAF11B | Ethernet32/1 | 172.17.1.71/31 | DC1-POD1-SPINE4 | Ethernet22/1 | 172.17.1.70/31 |
| DC1-POD1-LEAF12A | Ethernet29/1 | 172.17.1.73/31 | DC1-POD1-SPINE1 | Ethernet23/1 | 172.17.1.72/31 |
| DC1-POD1-LEAF12A | Ethernet30/1 | 172.17.1.75/31 | DC1-POD1-SPINE2 | Ethernet23/1 | 172.17.1.74/31 |
| DC1-POD1-LEAF12A | Ethernet31/1 | 172.17.1.77/31 | DC1-POD1-SPINE3 | Ethernet23/1 | 172.17.1.76/31 |
| DC1-POD1-LEAF12A | Ethernet32/1 | 172.17.1.79/31 | DC1-POD1-SPINE4 | Ethernet23/1 | 172.17.1.78/31 |
| DC1-POD1-LEAF12B | Ethernet29/1 | 172.17.1.81/31 | DC1-POD1-SPINE1 | Ethernet24/1 | 172.17.1.80/31 |
| DC1-POD1-LEAF12B | Ethernet30/1 | 172.17.1.83/31 | DC1-POD1-SPINE2 | Ethernet24/1 | 172.17.1.82/31 |
| DC1-POD1-LEAF12B | Ethernet31/1 | 172.17.1.85/31 | DC1-POD1-SPINE3 | Ethernet24/1 | 172.17.1.84/31 |
| DC1-POD1-LEAF12B | Ethernet32/1 | 172.17.1.87/31 | DC1-POD1-SPINE4 | Ethernet24/1 | 172.17.1.86/31 |
| DC1-POD1-LEAF13A | Ethernet29/1 | 172.17.1.89/31 | DC1-POD1-SPINE1 | Ethernet25/1 | 172.17.1.88/31 |
| DC1-POD1-LEAF13A | Ethernet30/1 | 172.17.1.91/31 | DC1-POD1-SPINE2 | Ethernet25/1 | 172.17.1.90/31 |
| DC1-POD1-LEAF13A | Ethernet31/1 | 172.17.1.93/31 | DC1-POD1-SPINE3 | Ethernet25/1 | 172.17.1.92/31 |
| DC1-POD1-LEAF13A | Ethernet32/1 | 172.17.1.95/31 | DC1-POD1-SPINE4 | Ethernet25/1 | 172.17.1.94/31 |
| DC1-POD1-LEAF13B | Ethernet29/1 | 172.17.1.97/31 | DC1-POD1-SPINE1 | Ethernet26/1 | 172.17.1.96/31 |
| DC1-POD1-LEAF13B | Ethernet30/1 | 172.17.1.99/31 | DC1-POD1-SPINE2 | Ethernet26/1 | 172.17.1.98/31 |
| DC1-POD1-LEAF13B | Ethernet31/1 | 172.17.1.101/31 | DC1-POD1-SPINE3 | Ethernet26/1 | 172.17.1.100/31 |
| DC1-POD1-LEAF13B | Ethernet32/1 | 172.17.1.103/31 | DC1-POD1-SPINE4 | Ethernet26/1 | 172.17.1.102/31 |
| DC1-POD1-LEAF14A | Ethernet29/1 | 172.17.1.105/31 | DC1-POD1-SPINE1 | Ethernet27/1 | 172.17.1.104/31 |
| DC1-POD1-LEAF14A | Ethernet30/1 | 172.17.1.107/31 | DC1-POD1-SPINE2 | Ethernet27/1 | 172.17.1.106/31 |
| DC1-POD1-LEAF14A | Ethernet31/1 | 172.17.1.109/31 | DC1-POD1-SPINE3 | Ethernet27/1 | 172.17.1.108/31 |
| DC1-POD1-LEAF14A | Ethernet32/1 | 172.17.1.111/31 | DC1-POD1-SPINE4 | Ethernet27/1 | 172.17.1.110/31 |
| DC1-POD1-LEAF14B | Ethernet29/1 | 172.17.1.113/31 | DC1-POD1-SPINE1 | Ethernet28/1 | 172.17.1.112/31 |
| DC1-POD1-LEAF14B | Ethernet30/1 | 172.17.1.115/31 | DC1-POD1-SPINE2 | Ethernet28/1 | 172.17.1.114/31 |
| DC1-POD1-LEAF14B | Ethernet31/1 | 172.17.1.117/31 | DC1-POD1-SPINE3 | Ethernet28/1 | 172.17.1.116/31 |
| DC1-POD1-LEAF14B | Ethernet32/1 | 172.17.1.119/31 | DC1-POD1-SPINE4 | Ethernet28/1 | 172.17.1.118/31 |
| DC1-POD1-SPINE1 | Ethernet29/1 | 172.16.0.19/31 | SUPER-SPINE1 | Ethernet1/1 | 172.16.0.18/31 |
| DC1-POD1-SPINE1 | Ethernet30/1 | 172.16.0.27/31 | SUPER-SPINE2 | Ethernet1/1 | 172.16.0.26/31 |
| DC1-POD1-SPINE1 | Ethernet31/1 | 172.16.0.35/31 | SUPER-SPINE3 | Ethernet1/1 | 172.16.0.34/31 |
| DC1-POD1-SPINE1 | Ethernet32/1 | 172.16.0.43/31 | SUPER-SPINE4 | Ethernet1/1 | 172.16.0.42/31 |
| DC1-POD1-SPINE2 | Ethernet29/1 | 172.16.0.21/31 | SUPER-SPINE1 | Ethernet2/1 | 172.16.0.20/31 |
| DC1-POD1-SPINE2 | Ethernet30/1 | 172.16.0.29/31 | SUPER-SPINE2 | Ethernet2/1 | 172.16.0.28/31 |
| DC1-POD1-SPINE2 | Ethernet31/1 | 172.16.0.37/31 | SUPER-SPINE3 | Ethernet2/1 | 172.16.0.36/31 |
| DC1-POD1-SPINE2 | Ethernet32/1 | 172.16.0.45/31 | SUPER-SPINE4 | Ethernet2/1 | 172.16.0.44/31 |
| DC1-POD1-SPINE3 | Ethernet29/1 | 172.16.0.23/31 | SUPER-SPINE1 | Ethernet3/1 | 172.16.0.22/31 |
| DC1-POD1-SPINE3 | Ethernet30/1 | 172.16.0.31/31 | SUPER-SPINE2 | Ethernet3/1 | 172.16.0.30/31 |
| DC1-POD1-SPINE3 | Ethernet31/1 | 172.16.0.39/31 | SUPER-SPINE3 | Ethernet3/1 | 172.16.0.38/31 |
| DC1-POD1-SPINE3 | Ethernet32/1 | 172.16.0.47/31 | SUPER-SPINE4 | Ethernet3/1 | 172.16.0.46/31 |
| DC1-POD1-SPINE4 | Ethernet29/1 | 172.16.0.25/31 | SUPER-SPINE1 | Ethernet4/1 | 172.16.0.24/31 |
| DC1-POD1-SPINE4 | Ethernet30/1 | 172.16.0.33/31 | SUPER-SPINE2 | Ethernet4/1 | 172.16.0.32/31 |
| DC1-POD1-SPINE4 | Ethernet31/1 | 172.16.0.41/31 | SUPER-SPINE3 | Ethernet4/1 | 172.16.0.40/31 |
| DC1-POD1-SPINE4 | Ethernet32/1 | 172.16.0.49/31 | SUPER-SPINE4 | Ethernet4/1 | 172.16.0.48/31 |
| DC1-POD2-LEAF1A | Ethernet29/1 | 172.17.32.153/31 | DC1-POD2-SPINE1 | Ethernet1/1 | 172.17.32.152/31 |
| DC1-POD2-LEAF1A | Ethernet30/1 | 172.17.32.155/31 | DC1-POD2-SPINE2 | Ethernet1/1 | 172.17.32.154/31 |
| DC1-POD2-LEAF1A | Ethernet31/1 | 172.17.32.157/31 | DC1-POD2-SPINE3 | Ethernet1/1 | 172.17.32.156/31 |
| DC1-POD2-LEAF1A | Ethernet32/1 | 172.17.32.159/31 | DC1-POD2-SPINE4 | Ethernet1/1 | 172.17.32.158/31 |
| DC1-POD2-LEAF1B | Ethernet29/1 | 172.17.32.161/31 | DC1-POD2-SPINE1 | Ethernet2/1 | 172.17.32.160/31 |
| DC1-POD2-LEAF1B | Ethernet30/1 | 172.17.32.163/31 | DC1-POD2-SPINE2 | Ethernet2/1 | 172.17.32.162/31 |
| DC1-POD2-LEAF1B | Ethernet31/1 | 172.17.32.165/31 | DC1-POD2-SPINE3 | Ethernet2/1 | 172.17.32.164/31 |
| DC1-POD2-LEAF1B | Ethernet32/1 | 172.17.32.167/31 | DC1-POD2-SPINE4 | Ethernet2/1 | 172.17.32.166/31 |
| DC1-POD2-LEAF2A | Ethernet29/1 | 172.17.32.169/31 | DC1-POD2-SPINE1 | Ethernet3/1 | 172.17.32.168/31 |
| DC1-POD2-LEAF2A | Ethernet30/1 | 172.17.32.171/31 | DC1-POD2-SPINE2 | Ethernet3/1 | 172.17.32.170/31 |
| DC1-POD2-LEAF2A | Ethernet31/1 | 172.17.32.173/31 | DC1-POD2-SPINE3 | Ethernet3/1 | 172.17.32.172/31 |
| DC1-POD2-LEAF2A | Ethernet32/1 | 172.17.32.175/31 | DC1-POD2-SPINE4 | Ethernet3/1 | 172.17.32.174/31 |
| DC1-POD2-LEAF2B | Ethernet29/1 | 172.17.32.177/31 | DC1-POD2-SPINE1 | Ethernet4/1 | 172.17.32.176/31 |
| DC1-POD2-LEAF2B | Ethernet30/1 | 172.17.32.179/31 | DC1-POD2-SPINE2 | Ethernet4/1 | 172.17.32.178/31 |
| DC1-POD2-LEAF2B | Ethernet31/1 | 172.17.32.181/31 | DC1-POD2-SPINE3 | Ethernet4/1 | 172.17.32.180/31 |
| DC1-POD2-LEAF2B | Ethernet32/1 | 172.17.32.183/31 | DC1-POD2-SPINE4 | Ethernet4/1 | 172.17.32.182/31 |
| DC1-POD2-LEAF3A | Ethernet29/1 | 172.17.32.185/31 | DC1-POD2-SPINE1 | Ethernet5/1 | 172.17.32.184/31 |
| DC1-POD2-LEAF3A | Ethernet30/1 | 172.17.32.187/31 | DC1-POD2-SPINE2 | Ethernet5/1 | 172.17.32.186/31 |
| DC1-POD2-LEAF3A | Ethernet31/1 | 172.17.32.189/31 | DC1-POD2-SPINE3 | Ethernet5/1 | 172.17.32.188/31 |
| DC1-POD2-LEAF3A | Ethernet32/1 | 172.17.32.191/31 | DC1-POD2-SPINE4 | Ethernet5/1 | 172.17.32.190/31 |
| DC1-POD2-LEAF3B | Ethernet29/1 | 172.17.32.193/31 | DC1-POD2-SPINE1 | Ethernet6/1 | 172.17.32.192/31 |
| DC1-POD2-LEAF3B | Ethernet30/1 | 172.17.32.195/31 | DC1-POD2-SPINE2 | Ethernet6/1 | 172.17.32.194/31 |
| DC1-POD2-LEAF3B | Ethernet31/1 | 172.17.32.197/31 | DC1-POD2-SPINE3 | Ethernet6/1 | 172.17.32.196/31 |
| DC1-POD2-LEAF3B | Ethernet32/1 | 172.17.32.199/31 | DC1-POD2-SPINE4 | Ethernet6/1 | 172.17.32.198/31 |
| DC1-POD2-LEAF4A | Ethernet29/1 | 172.17.32.201/31 | DC1-POD2-SPINE1 | Ethernet7/1 | 172.17.32.200/31 |
| DC1-POD2-LEAF4A | Ethernet30/1 | 172.17.32.203/31 | DC1-POD2-SPINE2 | Ethernet7/1 | 172.17.32.202/31 |
| DC1-POD2-LEAF4A | Ethernet31/1 | 172.17.32.205/31 | DC1-POD2-SPINE3 | Ethernet7/1 | 172.17.32.204/31 |
| DC1-POD2-LEAF4A | Ethernet32/1 | 172.17.32.207/31 | DC1-POD2-SPINE4 | Ethernet7/1 | 172.17.32.206/31 |
| DC1-POD2-LEAF4B | Ethernet29/1 | 172.17.32.209/31 | DC1-POD2-SPINE1 | Ethernet8/1 | 172.17.32.208/31 |
| DC1-POD2-LEAF4B | Ethernet30/1 | 172.17.32.211/31 | DC1-POD2-SPINE2 | Ethernet8/1 | 172.17.32.210/31 |
| DC1-POD2-LEAF4B | Ethernet31/1 | 172.17.32.213/31 | DC1-POD2-SPINE3 | Ethernet8/1 | 172.17.32.212/31 |
| DC1-POD2-LEAF4B | Ethernet32/1 | 172.17.32.215/31 | DC1-POD2-SPINE4 | Ethernet8/1 | 172.17.32.214/31 |
| DC1-POD2-LEAF5A | Ethernet29/1 | 172.17.32.217/31 | DC1-POD2-SPINE1 | Ethernet9/1 | 172.17.32.216/31 |
| DC1-POD2-LEAF5A | Ethernet30/1 | 172.17.32.219/31 | DC1-POD2-SPINE2 | Ethernet9/1 | 172.17.32.218/31 |
| DC1-POD2-LEAF5A | Ethernet31/1 | 172.17.32.221/31 | DC1-POD2-SPINE3 | Ethernet9/1 | 172.17.32.220/31 |
| DC1-POD2-LEAF5A | Ethernet32/1 | 172.17.32.223/31 | DC1-POD2-SPINE4 | Ethernet9/1 | 172.17.32.222/31 |
| DC1-POD2-LEAF5B | Ethernet29/1 | 172.17.32.225/31 | DC1-POD2-SPINE1 | Ethernet10/1 | 172.17.32.224/31 |
| DC1-POD2-LEAF5B | Ethernet30/1 | 172.17.32.227/31 | DC1-POD2-SPINE2 | Ethernet10/1 | 172.17.32.226/31 |
| DC1-POD2-LEAF5B | Ethernet31/1 | 172.17.32.229/31 | DC1-POD2-SPINE3 | Ethernet10/1 | 172.17.32.228/31 |
| DC1-POD2-LEAF5B | Ethernet32/1 | 172.17.32.231/31 | DC1-POD2-SPINE4 | Ethernet10/1 | 172.17.32.230/31 |
| DC1-POD2-LEAF6A | Ethernet29/1 | 172.17.32.233/31 | DC1-POD2-SPINE1 | Ethernet11/1 | 172.17.32.232/31 |
| DC1-POD2-LEAF6A | Ethernet30/1 | 172.17.32.235/31 | DC1-POD2-SPINE2 | Ethernet11/1 | 172.17.32.234/31 |
| DC1-POD2-LEAF6A | Ethernet31/1 | 172.17.32.237/31 | DC1-POD2-SPINE3 | Ethernet11/1 | 172.17.32.236/31 |
| DC1-POD2-LEAF6A | Ethernet32/1 | 172.17.32.239/31 | DC1-POD2-SPINE4 | Ethernet11/1 | 172.17.32.238/31 |
| DC1-POD2-LEAF6B | Ethernet29/1 | 172.17.32.241/31 | DC1-POD2-SPINE1 | Ethernet12/1 | 172.17.32.240/31 |
| DC1-POD2-LEAF6B | Ethernet30/1 | 172.17.32.243/31 | DC1-POD2-SPINE2 | Ethernet12/1 | 172.17.32.242/31 |
| DC1-POD2-LEAF6B | Ethernet31/1 | 172.17.32.245/31 | DC1-POD2-SPINE3 | Ethernet12/1 | 172.17.32.244/31 |
| DC1-POD2-LEAF6B | Ethernet32/1 | 172.17.32.247/31 | DC1-POD2-SPINE4 | Ethernet12/1 | 172.17.32.246/31 |
| DC1-POD2-LEAF7A | Ethernet29/1 | 172.17.32.249/31 | DC1-POD2-SPINE1 | Ethernet13/1 | 172.17.32.248/31 |
| DC1-POD2-LEAF7A | Ethernet30/1 | 172.17.32.251/31 | DC1-POD2-SPINE2 | Ethernet13/1 | 172.17.32.250/31 |
| DC1-POD2-LEAF7A | Ethernet31/1 | 172.17.32.253/31 | DC1-POD2-SPINE3 | Ethernet13/1 | 172.17.32.252/31 |
| DC1-POD2-LEAF7A | Ethernet32/1 | 172.17.32.255/31 | DC1-POD2-SPINE4 | Ethernet13/1 | 172.17.32.254/31 |
| DC1-POD2-LEAF7B | Ethernet29/1 | 172.17.33.1/31 | DC1-POD2-SPINE1 | Ethernet14/1 | 172.17.33.0/31 |
| DC1-POD2-LEAF7B | Ethernet30/1 | 172.17.33.3/31 | DC1-POD2-SPINE2 | Ethernet14/1 | 172.17.33.2/31 |
| DC1-POD2-LEAF7B | Ethernet31/1 | 172.17.33.5/31 | DC1-POD2-SPINE3 | Ethernet14/1 | 172.17.33.4/31 |
| DC1-POD2-LEAF7B | Ethernet32/1 | 172.17.33.7/31 | DC1-POD2-SPINE4 | Ethernet14/1 | 172.17.33.6/31 |
| DC1-POD2-LEAF8A | Ethernet29/1 | 172.17.33.9/31 | DC1-POD2-SPINE1 | Ethernet15/1 | 172.17.33.8/31 |
| DC1-POD2-LEAF8A | Ethernet30/1 | 172.17.33.11/31 | DC1-POD2-SPINE2 | Ethernet15/1 | 172.17.33.10/31 |
| DC1-POD2-LEAF8A | Ethernet31/1 | 172.17.33.13/31 | DC1-POD2-SPINE3 | Ethernet15/1 | 172.17.33.12/31 |
| DC1-POD2-LEAF8A | Ethernet32/1 | 172.17.33.15/31 | DC1-POD2-SPINE4 | Ethernet15/1 | 172.17.33.14/31 |
| DC1-POD2-LEAF8B | Ethernet29/1 | 172.17.33.17/31 | DC1-POD2-SPINE1 | Ethernet16/1 | 172.17.33.16/31 |
| DC1-POD2-LEAF8B | Ethernet30/1 | 172.17.33.19/31 | DC1-POD2-SPINE2 | Ethernet16/1 | 172.17.33.18/31 |
| DC1-POD2-LEAF8B | Ethernet31/1 | 172.17.33.21/31 | DC1-POD2-SPINE3 | Ethernet16/1 | 172.17.33.20/31 |
| DC1-POD2-LEAF8B | Ethernet32/1 | 172.17.33.23/31 | DC1-POD2-SPINE4 | Ethernet16/1 | 172.17.33.22/31 |
| DC1-POD2-LEAF9A | Ethernet29/1 | 172.17.33.25/31 | DC1-POD2-SPINE1 | Ethernet17/1 | 172.17.33.24/31 |
| DC1-POD2-LEAF9A | Ethernet30/1 | 172.17.33.27/31 | DC1-POD2-SPINE2 | Ethernet17/1 | 172.17.33.26/31 |
| DC1-POD2-LEAF9A | Ethernet31/1 | 172.17.33.29/31 | DC1-POD2-SPINE3 | Ethernet17/1 | 172.17.33.28/31 |
| DC1-POD2-LEAF9A | Ethernet32/1 | 172.17.33.31/31 | DC1-POD2-SPINE4 | Ethernet17/1 | 172.17.33.30/31 |
| DC1-POD2-LEAF9B | Ethernet29/1 | 172.17.33.33/31 | DC1-POD2-SPINE1 | Ethernet18/1 | 172.17.33.32/31 |
| DC1-POD2-LEAF9B | Ethernet30/1 | 172.17.33.35/31 | DC1-POD2-SPINE2 | Ethernet18/1 | 172.17.33.34/31 |
| DC1-POD2-LEAF9B | Ethernet31/1 | 172.17.33.37/31 | DC1-POD2-SPINE3 | Ethernet18/1 | 172.17.33.36/31 |
| DC1-POD2-LEAF9B | Ethernet32/1 | 172.17.33.39/31 | DC1-POD2-SPINE4 | Ethernet18/1 | 172.17.33.38/31 |
| DC1-POD2-LEAF10A | Ethernet29/1 | 172.17.33.41/31 | DC1-POD2-SPINE1 | Ethernet19/1 | 172.17.33.40/31 |
| DC1-POD2-LEAF10A | Ethernet30/1 | 172.17.33.43/31 | DC1-POD2-SPINE2 | Ethernet19/1 | 172.17.33.42/31 |
| DC1-POD2-LEAF10A | Ethernet31/1 | 172.17.33.45/31 | DC1-POD2-SPINE3 | Ethernet19/1 | 172.17.33.44/31 |
| DC1-POD2-LEAF10A | Ethernet32/1 | 172.17.33.47/31 | DC1-POD2-SPINE4 | Ethernet19/1 | 172.17.33.46/31 |
| DC1-POD2-LEAF10B | Ethernet29/1 | 172.17.33.49/31 | DC1-POD2-SPINE1 | Ethernet20/1 | 172.17.33.48/31 |
| DC1-POD2-LEAF10B | Ethernet30/1 | 172.17.33.51/31 | DC1-POD2-SPINE2 | Ethernet20/1 | 172.17.33.50/31 |
| DC1-POD2-LEAF10B | Ethernet31/1 | 172.17.33.53/31 | DC1-POD2-SPINE3 | Ethernet20/1 | 172.17.33.52/31 |
| DC1-POD2-LEAF10B | Ethernet32/1 | 172.17.33.55/31 | DC1-POD2-SPINE4 | Ethernet20/1 | 172.17.33.54/31 |
| DC1-POD2-LEAF11A | Ethernet29/1 | 172.17.33.57/31 | DC1-POD2-SPINE1 | Ethernet21/1 | 172.17.33.56/31 |
| DC1-POD2-LEAF11A | Ethernet30/1 | 172.17.33.59/31 | DC1-POD2-SPINE2 | Ethernet21/1 | 172.17.33.58/31 |
| DC1-POD2-LEAF11A | Ethernet31/1 | 172.17.33.61/31 | DC1-POD2-SPINE3 | Ethernet21/1 | 172.17.33.60/31 |
| DC1-POD2-LEAF11A | Ethernet32/1 | 172.17.33.63/31 | DC1-POD2-SPINE4 | Ethernet21/1 | 172.17.33.62/31 |
| DC1-POD2-LEAF11B | Ethernet29/1 | 172.17.33.65/31 | DC1-POD2-SPINE1 | Ethernet22/1 | 172.17.33.64/31 |
| DC1-POD2-LEAF11B | Ethernet30/1 | 172.17.33.67/31 | DC1-POD2-SPINE2 | Ethernet22/1 | 172.17.33.66/31 |
| DC1-POD2-LEAF11B | Ethernet31/1 | 172.17.33.69/31 | DC1-POD2-SPINE3 | Ethernet22/1 | 172.17.33.68/31 |
| DC1-POD2-LEAF11B | Ethernet32/1 | 172.17.33.71/31 | DC1-POD2-SPINE4 | Ethernet22/1 | 172.17.33.70/31 |
| DC1-POD2-LEAF12A | Ethernet29/1 | 172.17.33.73/31 | DC1-POD2-SPINE1 | Ethernet23/1 | 172.17.33.72/31 |
| DC1-POD2-LEAF12A | Ethernet30/1 | 172.17.33.75/31 | DC1-POD2-SPINE2 | Ethernet23/1 | 172.17.33.74/31 |
| DC1-POD2-LEAF12A | Ethernet31/1 | 172.17.33.77/31 | DC1-POD2-SPINE3 | Ethernet23/1 | 172.17.33.76/31 |
| DC1-POD2-LEAF12A | Ethernet32/1 | 172.17.33.79/31 | DC1-POD2-SPINE4 | Ethernet23/1 | 172.17.33.78/31 |
| DC1-POD2-LEAF12B | Ethernet29/1 | 172.17.33.81/31 | DC1-POD2-SPINE1 | Ethernet24/1 | 172.17.33.80/31 |
| DC1-POD2-LEAF12B | Ethernet30/1 | 172.17.33.83/31 | DC1-POD2-SPINE2 | Ethernet24/1 | 172.17.33.82/31 |
| DC1-POD2-LEAF12B | Ethernet31/1 | 172.17.33.85/31 | DC1-POD2-SPINE3 | Ethernet24/1 | 172.17.33.84/31 |
| DC1-POD2-LEAF12B | Ethernet32/1 | 172.17.33.87/31 | DC1-POD2-SPINE4 | Ethernet24/1 | 172.17.33.86/31 |
| DC1-POD2-LEAF13A | Ethernet29/1 | 172.17.33.89/31 | DC1-POD2-SPINE1 | Ethernet25/1 | 172.17.33.88/31 |
| DC1-POD2-LEAF13A | Ethernet30/1 | 172.17.33.91/31 | DC1-POD2-SPINE2 | Ethernet25/1 | 172.17.33.90/31 |
| DC1-POD2-LEAF13A | Ethernet31/1 | 172.17.33.93/31 | DC1-POD2-SPINE3 | Ethernet25/1 | 172.17.33.92/31 |
| DC1-POD2-LEAF13A | Ethernet32/1 | 172.17.33.95/31 | DC1-POD2-SPINE4 | Ethernet25/1 | 172.17.33.94/31 |
| DC1-POD2-LEAF13B | Ethernet29/1 | 172.17.33.97/31 | DC1-POD2-SPINE1 | Ethernet26/1 | 172.17.33.96/31 |
| DC1-POD2-LEAF13B | Ethernet30/1 | 172.17.33.99/31 | DC1-POD2-SPINE2 | Ethernet26/1 | 172.17.33.98/31 |
| DC1-POD2-LEAF13B | Ethernet31/1 | 172.17.33.101/31 | DC1-POD2-SPINE3 | Ethernet26/1 | 172.17.33.100/31 |
| DC1-POD2-LEAF13B | Ethernet32/1 | 172.17.33.103/31 | DC1-POD2-SPINE4 | Ethernet26/1 | 172.17.33.102/31 |
| DC1-POD2-LEAF14A | Ethernet29/1 | 172.17.33.105/31 | DC1-POD2-SPINE1 | Ethernet27/1 | 172.17.33.104/31 |
| DC1-POD2-LEAF14A | Ethernet30/1 | 172.17.33.107/31 | DC1-POD2-SPINE2 | Ethernet27/1 | 172.17.33.106/31 |
| DC1-POD2-LEAF14A | Ethernet31/1 | 172.17.33.109/31 | DC1-POD2-SPINE3 | Ethernet27/1 | 172.17.33.108/31 |
| DC1-POD2-LEAF14A | Ethernet32/1 | 172.17.33.111/31 | DC1-POD2-SPINE4 | Ethernet27/1 | 172.17.33.110/31 |
| DC1-POD2-LEAF14B | Ethernet29/1 | 172.17.33.113/31 | DC1-POD2-SPINE1 | Ethernet28/1 | 172.17.33.112/31 |
| DC1-POD2-LEAF14B | Ethernet30/1 | 172.17.33.115/31 | DC1-POD2-SPINE2 | Ethernet28/1 | 172.17.33.114/31 |
| DC1-POD2-LEAF14B | Ethernet31/1 | 172.17.33.117/31 | DC1-POD2-SPINE3 | Ethernet28/1 | 172.17.33.116/31 |
| DC1-POD2-LEAF14B | Ethernet32/1 | 172.17.33.119/31 | DC1-POD2-SPINE4 | Ethernet28/1 | 172.17.33.118/31 |
| DC1-POD2-SPINE1 | Ethernet29/1 | 172.16.32.19/31 | SUPER-SPINE1 | Ethernet5/1 | 172.16.32.18/31 |
| DC1-POD2-SPINE1 | Ethernet30/1 | 172.16.32.83/31 | SUPER-SPINE2 | Ethernet5/1 | 172.16.32.82/31 |
| DC1-POD2-SPINE1 | Ethernet31/1 | 172.16.32.147/31 | SUPER-SPINE3 | Ethernet5/1 | 172.16.32.146/31 |
| DC1-POD2-SPINE1 | Ethernet32/1 | 172.16.32.211/31 | SUPER-SPINE4 | Ethernet5/2 | 172.16.32.210/31 |
| DC1-POD2-SPINE2 | Ethernet29/1 | 172.16.32.23/31 | SUPER-SPINE1 | Ethernet6/1 | 172.16.32.22/31 |
| DC1-POD2-SPINE2 | Ethernet30/1 | 172.16.32.87/31 | SUPER-SPINE2 | Ethernet6/1 | 172.16.32.86/31 |
| DC1-POD2-SPINE2 | Ethernet31/1 | 172.16.32.151/31 | SUPER-SPINE3 | Ethernet6/1 | 172.16.32.150/31 |
| DC1-POD2-SPINE2 | Ethernet32/1 | 172.16.32.215/31 | SUPER-SPINE4 | Ethernet6/1 | 172.16.32.214/31 |
| DC1-POD2-SPINE3 | Ethernet29/1 | 172.16.32.5/31 | SUPER-SPINE1 | Ethernet7/1 | 172.16.32.4/31 |
| DC1-POD2-SPINE3 | Ethernet30/1 | 172.16.32.69/31 | SUPER-SPINE2 | Ethernet7/1 | 172.16.32.68/31 |
| DC1-POD2-SPINE3 | Ethernet31/1 | 172.16.32.133/31 | SUPER-SPINE3 | Ethernet7/1 | 172.16.32.132/31 |
| DC1-POD2-SPINE3 | Ethernet32/1 | 172.16.32.197/31 | SUPER-SPINE4 | Ethernet7/1 | 172.16.32.196/31 |
| DC1-POD2-SPINE4 | Ethernet29/1 | 172.16.32.7/31 | SUPER-SPINE1 | Ethernet8/1 | 172.16.32.6/31 |
| DC1-POD2-SPINE4 | Ethernet30/1 | 172.16.32.71/31 | SUPER-SPINE2 | Ethernet8/1 | 172.16.32.70/31 |
| DC1-POD2-SPINE4 | Ethernet31/1 | 172.16.32.135/31 | SUPER-SPINE3 | Ethernet8/1 | 172.16.32.134/31 |
| DC1-POD2-SPINE4 | Ethernet32/1 | 172.16.32.199/31 | SUPER-SPINE4 | Ethernet8/1 | 172.16.32.198/31 |
| DC2-POD1-LEAF1A | Ethernet29/1 | 172.17.64.153/31 | DC2-POD1-SPINE1 | Ethernet1/1 | 172.17.64.152/31 |
| DC2-POD1-LEAF1A | Ethernet30/1 | 172.17.64.155/31 | DC2-POD1-SPINE2 | Ethernet1/1 | 172.17.64.154/31 |
| DC2-POD1-LEAF1A | Ethernet31/1 | 172.17.64.157/31 | DC2-POD1-SPINE3 | Ethernet1/1 | 172.17.64.156/31 |
| DC2-POD1-LEAF1A | Ethernet32/1 | 172.17.64.159/31 | DC2-POD1-SPINE4 | Ethernet1/1 | 172.17.64.158/31 |
| DC2-POD1-LEAF1B | Ethernet29/1 | 172.17.64.161/31 | DC2-POD1-SPINE1 | Ethernet2/1 | 172.17.64.160/31 |
| DC2-POD1-LEAF1B | Ethernet30/1 | 172.17.64.163/31 | DC2-POD1-SPINE2 | Ethernet2/1 | 172.17.64.162/31 |
| DC2-POD1-LEAF1B | Ethernet31/1 | 172.17.64.165/31 | DC2-POD1-SPINE3 | Ethernet2/1 | 172.17.64.164/31 |
| DC2-POD1-LEAF1B | Ethernet32/1 | 172.17.64.167/31 | DC2-POD1-SPINE4 | Ethernet2/1 | 172.17.64.166/31 |
| DC2-POD1-LEAF2A | Ethernet29/1 | 172.17.64.177/31 | DC2-POD1-SPINE1 | Ethernet3/1 | 172.17.64.176/31 |
| DC2-POD1-LEAF2A | Ethernet30/1 | 172.17.64.179/31 | DC2-POD1-SPINE2 | Ethernet3/1 | 172.17.64.178/31 |
| DC2-POD1-LEAF2A | Ethernet31/1 | 172.17.64.181/31 | DC2-POD1-SPINE3 | Ethernet3/1 | 172.17.64.180/31 |
| DC2-POD1-LEAF2A | Ethernet32/1 | 172.17.64.183/31 | DC2-POD1-SPINE4 | Ethernet3/1 | 172.17.64.182/31 |
| DC2-POD1-LEAF2B | Ethernet29/1 | 172.17.64.185/31 | DC2-POD1-SPINE1 | Ethernet4/1 | 172.17.64.184/31 |
| DC2-POD1-LEAF2B | Ethernet30/1 | 172.17.64.187/31 | DC2-POD1-SPINE2 | Ethernet4/1 | 172.17.64.186/31 |
| DC2-POD1-LEAF2B | Ethernet31/1 | 172.17.64.189/31 | DC2-POD1-SPINE3 | Ethernet4/1 | 172.17.64.188/31 |
| DC2-POD1-LEAF2B | Ethernet32/1 | 172.17.64.191/31 | DC2-POD1-SPINE4 | Ethernet4/1 | 172.17.64.190/31 |
| DC2-POD1-LEAF3A | Ethernet29/1 | 172.17.64.193/31 | DC2-POD1-SPINE1 | Ethernet5/1 | 172.17.64.192/31 |
| DC2-POD1-LEAF3A | Ethernet30/1 | 172.17.64.195/31 | DC2-POD1-SPINE2 | Ethernet5/1 | 172.17.64.194/31 |
| DC2-POD1-LEAF3A | Ethernet31/1 | 172.17.64.197/31 | DC2-POD1-SPINE3 | Ethernet5/1 | 172.17.64.196/31 |
| DC2-POD1-LEAF3A | Ethernet32/1 | 172.17.64.199/31 | DC2-POD1-SPINE4 | Ethernet5/1 | 172.17.64.198/31 |
| DC2-POD1-LEAF3B | Ethernet29/1 | 172.17.64.201/31 | DC2-POD1-SPINE1 | Ethernet6/1 | 172.17.64.200/31 |
| DC2-POD1-LEAF3B | Ethernet30/1 | 172.17.64.203/31 | DC2-POD1-SPINE2 | Ethernet6/1 | 172.17.64.202/31 |
| DC2-POD1-LEAF3B | Ethernet31/1 | 172.17.64.205/31 | DC2-POD1-SPINE3 | Ethernet6/1 | 172.17.64.204/31 |
| DC2-POD1-LEAF3B | Ethernet32/1 | 172.17.64.207/31 | DC2-POD1-SPINE4 | Ethernet6/1 | 172.17.64.206/31 |
| DC2-POD1-LEAF4A | Ethernet29/1 | 172.17.64.209/31 | DC2-POD1-SPINE1 | Ethernet7/1 | 172.17.64.208/31 |
| DC2-POD1-LEAF4A | Ethernet30/1 | 172.17.64.211/31 | DC2-POD1-SPINE2 | Ethernet7/1 | 172.17.64.210/31 |
| DC2-POD1-LEAF4A | Ethernet31/1 | 172.17.64.213/31 | DC2-POD1-SPINE3 | Ethernet7/1 | 172.17.64.212/31 |
| DC2-POD1-LEAF4A | Ethernet32/1 | 172.17.64.215/31 | DC2-POD1-SPINE4 | Ethernet7/1 | 172.17.64.214/31 |
| DC2-POD1-LEAF4B | Ethernet29/1 | 172.17.64.217/31 | DC2-POD1-SPINE1 | Ethernet8/1 | 172.17.64.216/31 |
| DC2-POD1-LEAF4B | Ethernet30/1 | 172.17.64.219/31 | DC2-POD1-SPINE2 | Ethernet8/1 | 172.17.64.218/31 |
| DC2-POD1-LEAF4B | Ethernet31/1 | 172.17.64.221/31 | DC2-POD1-SPINE3 | Ethernet8/1 | 172.17.64.220/31 |
| DC2-POD1-LEAF4B | Ethernet32/1 | 172.17.64.223/31 | DC2-POD1-SPINE4 | Ethernet8/1 | 172.17.64.222/31 |
| DC2-POD1-LEAF5A | Ethernet29/1 | 172.17.64.225/31 | DC2-POD1-SPINE1 | Ethernet9/1 | 172.17.64.224/31 |
| DC2-POD1-LEAF5A | Ethernet30/1 | 172.17.64.227/31 | DC2-POD1-SPINE2 | Ethernet9/1 | 172.17.64.226/31 |
| DC2-POD1-LEAF5A | Ethernet31/1 | 172.17.64.229/31 | DC2-POD1-SPINE3 | Ethernet9/1 | 172.17.64.228/31 |
| DC2-POD1-LEAF5A | Ethernet32/1 | 172.17.64.231/31 | DC2-POD1-SPINE4 | Ethernet9/1 | 172.17.64.230/31 |
| DC2-POD1-LEAF5B | Ethernet29/1 | 172.17.64.233/31 | DC2-POD1-SPINE1 | Ethernet10/1 | 172.17.64.232/31 |
| DC2-POD1-LEAF5B | Ethernet30/1 | 172.17.64.235/31 | DC2-POD1-SPINE2 | Ethernet10/1 | 172.17.64.234/31 |
| DC2-POD1-LEAF5B | Ethernet31/1 | 172.17.64.237/31 | DC2-POD1-SPINE3 | Ethernet10/1 | 172.17.64.236/31 |
| DC2-POD1-LEAF5B | Ethernet32/1 | 172.17.64.239/31 | DC2-POD1-SPINE4 | Ethernet10/1 | 172.17.64.238/31 |
| DC2-POD1-LEAF6A | Ethernet29/1 | 172.17.64.241/31 | DC2-POD1-SPINE1 | Ethernet11/1 | 172.17.64.240/31 |
| DC2-POD1-LEAF6A | Ethernet30/1 | 172.17.64.243/31 | DC2-POD1-SPINE2 | Ethernet11/1 | 172.17.64.242/31 |
| DC2-POD1-LEAF6A | Ethernet31/1 | 172.17.64.245/31 | DC2-POD1-SPINE3 | Ethernet11/1 | 172.17.64.244/31 |
| DC2-POD1-LEAF6A | Ethernet32/1 | 172.17.64.247/31 | DC2-POD1-SPINE4 | Ethernet11/1 | 172.17.64.246/31 |
| DC2-POD1-LEAF6B | Ethernet29/1 | 172.17.64.249/31 | DC2-POD1-SPINE1 | Ethernet12/1 | 172.17.64.248/31 |
| DC2-POD1-LEAF6B | Ethernet30/1 | 172.17.64.251/31 | DC2-POD1-SPINE2 | Ethernet12/1 | 172.17.64.250/31 |
| DC2-POD1-LEAF6B | Ethernet31/1 | 172.17.64.253/31 | DC2-POD1-SPINE3 | Ethernet12/1 | 172.17.64.252/31 |
| DC2-POD1-LEAF6B | Ethernet32/1 | 172.17.64.255/31 | DC2-POD1-SPINE4 | Ethernet12/1 | 172.17.64.254/31 |
| DC2-POD1-LEAF7A | Ethernet29/1 | 172.17.65.1/31 | DC2-POD1-SPINE1 | Ethernet13/1 | 172.17.65.0/31 |
| DC2-POD1-LEAF7A | Ethernet30/1 | 172.17.65.3/31 | DC2-POD1-SPINE2 | Ethernet13/1 | 172.17.65.2/31 |
| DC2-POD1-LEAF7A | Ethernet31/1 | 172.17.65.5/31 | DC2-POD1-SPINE3 | Ethernet13/1 | 172.17.65.4/31 |
| DC2-POD1-LEAF7A | Ethernet32/1 | 172.17.65.7/31 | DC2-POD1-SPINE4 | Ethernet13/1 | 172.17.65.6/31 |
| DC2-POD1-LEAF7B | Ethernet29/1 | 172.17.65.9/31 | DC2-POD1-SPINE1 | Ethernet14/1 | 172.17.65.8/31 |
| DC2-POD1-LEAF7B | Ethernet30/1 | 172.17.65.11/31 | DC2-POD1-SPINE2 | Ethernet14/1 | 172.17.65.10/31 |
| DC2-POD1-LEAF7B | Ethernet31/1 | 172.17.65.13/31 | DC2-POD1-SPINE3 | Ethernet14/1 | 172.17.65.12/31 |
| DC2-POD1-LEAF7B | Ethernet32/1 | 172.17.65.15/31 | DC2-POD1-SPINE4 | Ethernet14/1 | 172.17.65.14/31 |
| DC2-POD1-LEAF8A | Ethernet29/1 | 172.17.65.17/31 | DC2-POD1-SPINE1 | Ethernet15/1 | 172.17.65.16/31 |
| DC2-POD1-LEAF8A | Ethernet30/1 | 172.17.65.19/31 | DC2-POD1-SPINE2 | Ethernet15/1 | 172.17.65.18/31 |
| DC2-POD1-LEAF8A | Ethernet31/1 | 172.17.65.21/31 | DC2-POD1-SPINE3 | Ethernet15/1 | 172.17.65.20/31 |
| DC2-POD1-LEAF8A | Ethernet32/1 | 172.17.65.23/31 | DC2-POD1-SPINE4 | Ethernet15/1 | 172.17.65.22/31 |
| DC2-POD1-LEAF8B | Ethernet29/1 | 172.17.65.25/31 | DC2-POD1-SPINE1 | Ethernet16/1 | 172.17.65.24/31 |
| DC2-POD1-LEAF8B | Ethernet30/1 | 172.17.65.27/31 | DC2-POD1-SPINE2 | Ethernet16/1 | 172.17.65.26/31 |
| DC2-POD1-LEAF8B | Ethernet31/1 | 172.17.65.29/31 | DC2-POD1-SPINE3 | Ethernet16/1 | 172.17.65.28/31 |
| DC2-POD1-LEAF8B | Ethernet32/1 | 172.17.65.31/31 | DC2-POD1-SPINE4 | Ethernet16/1 | 172.17.65.30/31 |
| DC2-POD1-LEAF9A | Ethernet29/1 | 172.17.65.33/31 | DC2-POD1-SPINE1 | Ethernet17/1 | 172.17.65.32/31 |
| DC2-POD1-LEAF9A | Ethernet30/1 | 172.17.65.35/31 | DC2-POD1-SPINE2 | Ethernet17/1 | 172.17.65.34/31 |
| DC2-POD1-LEAF9A | Ethernet31/1 | 172.17.65.37/31 | DC2-POD1-SPINE3 | Ethernet17/1 | 172.17.65.36/31 |
| DC2-POD1-LEAF9A | Ethernet32/1 | 172.17.65.39/31 | DC2-POD1-SPINE4 | Ethernet17/1 | 172.17.65.38/31 |
| DC2-POD1-LEAF9B | Ethernet29/1 | 172.17.65.41/31 | DC2-POD1-SPINE1 | Ethernet18/1 | 172.17.65.40/31 |
| DC2-POD1-LEAF9B | Ethernet30/1 | 172.17.65.43/31 | DC2-POD1-SPINE2 | Ethernet18/1 | 172.17.65.42/31 |
| DC2-POD1-LEAF9B | Ethernet31/1 | 172.17.65.45/31 | DC2-POD1-SPINE3 | Ethernet18/1 | 172.17.65.44/31 |
| DC2-POD1-LEAF9B | Ethernet32/1 | 172.17.65.47/31 | DC2-POD1-SPINE4 | Ethernet18/1 | 172.17.65.46/31 |
| DC2-POD1-LEAF10A | Ethernet29/1 | 172.17.65.49/31 | DC2-POD1-SPINE1 | Ethernet19/1 | 172.17.65.48/31 |
| DC2-POD1-LEAF10A | Ethernet30/1 | 172.17.65.51/31 | DC2-POD1-SPINE2 | Ethernet19/1 | 172.17.65.50/31 |
| DC2-POD1-LEAF10A | Ethernet31/1 | 172.17.65.53/31 | DC2-POD1-SPINE3 | Ethernet19/1 | 172.17.65.52/31 |
| DC2-POD1-LEAF10A | Ethernet32/1 | 172.17.65.55/31 | DC2-POD1-SPINE4 | Ethernet19/1 | 172.17.65.54/31 |
| DC2-POD1-LEAF10B | Ethernet29/1 | 172.17.65.57/31 | DC2-POD1-SPINE1 | Ethernet20/1 | 172.17.65.56/31 |
| DC2-POD1-LEAF10B | Ethernet30/1 | 172.17.65.59/31 | DC2-POD1-SPINE2 | Ethernet20/1 | 172.17.65.58/31 |
| DC2-POD1-LEAF10B | Ethernet31/1 | 172.17.65.61/31 | DC2-POD1-SPINE3 | Ethernet20/1 | 172.17.65.60/31 |
| DC2-POD1-LEAF10B | Ethernet32/1 | 172.17.65.63/31 | DC2-POD1-SPINE4 | Ethernet20/1 | 172.17.65.62/31 |
| DC2-POD1-LEAF11A | Ethernet29/1 | 172.17.65.65/31 | DC2-POD1-SPINE1 | Ethernet21/1 | 172.17.65.64/31 |
| DC2-POD1-LEAF11A | Ethernet30/1 | 172.17.65.67/31 | DC2-POD1-SPINE2 | Ethernet21/1 | 172.17.65.66/31 |
| DC2-POD1-LEAF11A | Ethernet31/1 | 172.17.65.69/31 | DC2-POD1-SPINE3 | Ethernet21/1 | 172.17.65.68/31 |
| DC2-POD1-LEAF11A | Ethernet32/1 | 172.17.65.71/31 | DC2-POD1-SPINE4 | Ethernet21/1 | 172.17.65.70/31 |
| DC2-POD1-LEAF11B | Ethernet29/1 | 172.17.65.73/31 | DC2-POD1-SPINE1 | Ethernet22/1 | 172.17.65.72/31 |
| DC2-POD1-LEAF11B | Ethernet30/1 | 172.17.65.75/31 | DC2-POD1-SPINE2 | Ethernet22/1 | 172.17.65.74/31 |
| DC2-POD1-LEAF11B | Ethernet31/1 | 172.17.65.77/31 | DC2-POD1-SPINE3 | Ethernet22/1 | 172.17.65.76/31 |
| DC2-POD1-LEAF11B | Ethernet32/1 | 172.17.65.79/31 | DC2-POD1-SPINE4 | Ethernet22/1 | 172.17.65.78/31 |
| DC2-POD1-LEAF12A | Ethernet29/1 | 172.17.65.81/31 | DC2-POD1-SPINE1 | Ethernet23/1 | 172.17.65.80/31 |
| DC2-POD1-LEAF12A | Ethernet30/1 | 172.17.65.83/31 | DC2-POD1-SPINE2 | Ethernet23/1 | 172.17.65.82/31 |
| DC2-POD1-LEAF12A | Ethernet31/1 | 172.17.65.85/31 | DC2-POD1-SPINE3 | Ethernet23/1 | 172.17.65.84/31 |
| DC2-POD1-LEAF12A | Ethernet32/1 | 172.17.65.87/31 | DC2-POD1-SPINE4 | Ethernet23/1 | 172.17.65.86/31 |
| DC2-POD1-LEAF12B | Ethernet29/1 | 172.17.65.89/31 | DC2-POD1-SPINE1 | Ethernet24/1 | 172.17.65.88/31 |
| DC2-POD1-LEAF12B | Ethernet30/1 | 172.17.65.91/31 | DC2-POD1-SPINE2 | Ethernet24/1 | 172.17.65.90/31 |
| DC2-POD1-LEAF12B | Ethernet31/1 | 172.17.65.93/31 | DC2-POD1-SPINE3 | Ethernet24/1 | 172.17.65.92/31 |
| DC2-POD1-LEAF12B | Ethernet32/1 | 172.17.65.95/31 | DC2-POD1-SPINE4 | Ethernet24/1 | 172.17.65.94/31 |
| DC2-POD1-LEAF13A | Ethernet29/1 | 172.17.65.97/31 | DC2-POD1-SPINE1 | Ethernet25/1 | 172.17.65.96/31 |
| DC2-POD1-LEAF13A | Ethernet30/1 | 172.17.65.99/31 | DC2-POD1-SPINE2 | Ethernet25/1 | 172.17.65.98/31 |
| DC2-POD1-LEAF13A | Ethernet31/1 | 172.17.65.101/31 | DC2-POD1-SPINE3 | Ethernet25/1 | 172.17.65.100/31 |
| DC2-POD1-LEAF13A | Ethernet32/1 | 172.17.65.103/31 | DC2-POD1-SPINE4 | Ethernet25/1 | 172.17.65.102/31 |
| DC2-POD1-LEAF13B | Ethernet29/1 | 172.17.65.105/31 | DC2-POD1-SPINE1 | Ethernet26/1 | 172.17.65.104/31 |
| DC2-POD1-LEAF13B | Ethernet30/1 | 172.17.65.107/31 | DC2-POD1-SPINE2 | Ethernet26/1 | 172.17.65.106/31 |
| DC2-POD1-LEAF13B | Ethernet31/1 | 172.17.65.109/31 | DC2-POD1-SPINE3 | Ethernet26/1 | 172.17.65.108/31 |
| DC2-POD1-LEAF13B | Ethernet32/1 | 172.17.65.111/31 | DC2-POD1-SPINE4 | Ethernet26/1 | 172.17.65.110/31 |
| DC2-POD1-LEAF14A | Ethernet29/1 | 172.17.65.113/31 | DC2-POD1-SPINE1 | Ethernet27/1 | 172.17.65.112/31 |
| DC2-POD1-LEAF14A | Ethernet30/1 | 172.17.65.115/31 | DC2-POD1-SPINE2 | Ethernet27/1 | 172.17.65.114/31 |
| DC2-POD1-LEAF14A | Ethernet31/1 | 172.17.65.117/31 | DC2-POD1-SPINE3 | Ethernet27/1 | 172.17.65.116/31 |
| DC2-POD1-LEAF14A | Ethernet32/1 | 172.17.65.119/31 | DC2-POD1-SPINE4 | Ethernet27/1 | 172.17.65.118/31 |
| DC2-POD1-LEAF14B | Ethernet29/1 | 172.17.65.121/31 | DC2-POD1-SPINE1 | Ethernet28/1 | 172.17.65.120/31 |
| DC2-POD1-LEAF14B | Ethernet30/1 | 172.17.65.123/31 | DC2-POD1-SPINE2 | Ethernet28/1 | 172.17.65.122/31 |
| DC2-POD1-LEAF14B | Ethernet31/1 | 172.17.65.125/31 | DC2-POD1-SPINE3 | Ethernet28/1 | 172.17.65.124/31 |
| DC2-POD1-LEAF14B | Ethernet32/1 | 172.17.65.127/31 | DC2-POD1-SPINE4 | Ethernet28/1 | 172.17.65.126/31 |
| DC2-POD1-SPINE1 | Ethernet29/1 | 172.16.64.19/31 | SUPER-SPINE1 | Ethernet9/1 | 172.16.64.18/31 |
| DC2-POD1-SPINE1 | Ethernet30/1 | 172.16.64.83/31 | SUPER-SPINE2 | Ethernet9/1 | 172.16.64.82/31 |
| DC2-POD1-SPINE1 | Ethernet31/1 | 172.16.64.147/31 | SUPER-SPINE3 | Ethernet9/1 | 172.16.64.146/31 |
| DC2-POD1-SPINE1 | Ethernet32/1 | 172.16.64.211/31 | SUPER-SPINE4 | Ethernet9/1 | 172.16.64.210/31 |
| DC2-POD1-SPINE2 | Ethernet29/1 | 172.16.64.23/31 | SUPER-SPINE1 | Ethernet10/1 | 172.16.64.22/31 |
| DC2-POD1-SPINE2 | Ethernet30/1 | 172.16.64.87/31 | SUPER-SPINE2 | Ethernet10/1 | 172.16.64.86/31 |
| DC2-POD1-SPINE2 | Ethernet31/1 | 172.16.64.151/31 | SUPER-SPINE3 | Ethernet10/1 | 172.16.64.150/31 |
| DC2-POD1-SPINE2 | Ethernet32/1 | 172.16.64.215/31 | SUPER-SPINE4 | Ethernet10/1 | 172.16.64.214/31 |
| DC2-POD1-SPINE3 | Ethernet29/1 | 172.16.64.25/31 | SUPER-SPINE1 | Ethernet11/1 | 172.16.64.24/31 |
| DC2-POD1-SPINE3 | Ethernet30/1 | 172.16.64.89/31 | SUPER-SPINE2 | Ethernet11/1 | 172.16.64.88/31 |
| DC2-POD1-SPINE3 | Ethernet31/1 | 172.16.64.153/31 | SUPER-SPINE3 | Ethernet11/1 | 172.16.64.152/31 |
| DC2-POD1-SPINE3 | Ethernet32/1 | 172.16.64.217/31 | SUPER-SPINE4 | Ethernet11/1 | 172.16.64.216/31 |
| DC2-POD1-SPINE4 | Ethernet29/1 | 172.16.64.27/31 | SUPER-SPINE1 | Ethernet12/1 | 172.16.64.26/31 |
| DC2-POD1-SPINE4 | Ethernet30/1 | 172.16.64.91/31 | SUPER-SPINE2 | Ethernet12/1 | 172.16.64.90/31 |
| DC2-POD1-SPINE4 | Ethernet31/1 | 172.16.64.155/31 | SUPER-SPINE3 | Ethernet12/1 | 172.16.64.154/31 |
| DC2-POD1-SPINE4 | Ethernet32/1 | 172.16.64.219/31 | SUPER-SPINE4 | Ethernet12/1 | 172.16.64.218/31 |

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.4.0.0/24 | 256 | 4 | 1.57 % |
| 10.4.1.0/24 | 256 | 28 | 10.94 % |
| 10.4.27.0/24 | 256 | 5 | 1.96 % |
| 10.4.32.0/24 | 256 | 4 | 1.57 % |
| 10.4.33.0/24 | 256 | 28 | 10.94 % |
| 10.4.64.0/24 | 256 | 4 | 1.57 % |
| 10.4.65.0/24 | 256 | 28 | 10.94 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC1_POD1 | DC1-POD1-LEAF1A | 10.4.1.22/32 |
| DC1_POD1 | DC1-POD1-LEAF1B | 10.4.1.23/32 |
| DC1_POD1 | DC1-POD1-LEAF2A | 10.4.1.24/32 |
| DC1_POD1 | DC1-POD1-LEAF2B | 10.4.1.25/32 |
| DC1_POD1 | DC1-POD1-LEAF3A | 10.4.1.26/32 |
| DC1_POD1 | DC1-POD1-LEAF3B | 10.4.1.27/32 |
| DC1_POD1 | DC1-POD1-LEAF4A | 10.4.1.28/32 |
| DC1_POD1 | DC1-POD1-LEAF4B | 10.4.1.29/32 |
| DC1_POD1 | DC1-POD1-LEAF5A | 10.4.1.30/32 |
| DC1_POD1 | DC1-POD1-LEAF5B | 10.4.1.31/32 |
| DC1_POD1 | DC1-POD1-LEAF6A | 10.4.1.32/32 |
| DC1_POD1 | DC1-POD1-LEAF6B | 10.4.1.33/32 |
| DC1_POD1 | DC1-POD1-LEAF7A | 10.4.1.34/32 |
| DC1_POD1 | DC1-POD1-LEAF7B | 10.4.1.35/32 |
| DC1_POD1 | DC1-POD1-LEAF8A | 10.4.1.36/32 |
| DC1_POD1 | DC1-POD1-LEAF8B | 10.4.1.37/32 |
| DC1_POD1 | DC1-POD1-LEAF9A | 10.4.1.38/32 |
| DC1_POD1 | DC1-POD1-LEAF9B | 10.4.1.39/32 |
| DC1_POD1 | DC1-POD1-LEAF10A | 10.4.1.40/32 |
| DC1_POD1 | DC1-POD1-LEAF10B | 10.4.1.41/32 |
| DC1_POD1 | DC1-POD1-LEAF11A | 10.4.1.42/32 |
| DC1_POD1 | DC1-POD1-LEAF11B | 10.4.1.43/32 |
| DC1_POD1 | DC1-POD1-LEAF12A | 10.4.1.44/32 |
| DC1_POD1 | DC1-POD1-LEAF12B | 10.4.1.45/32 |
| DC1_POD1 | DC1-POD1-LEAF13A | 10.4.1.46/32 |
| DC1_POD1 | DC1-POD1-LEAF13B | 10.4.1.47/32 |
| DC1_POD1 | DC1-POD1-LEAF14A | 10.4.1.48/32 |
| DC1_POD1 | DC1-POD1-LEAF14B | 10.4.1.49/32 |
| DC1_POD1 | DC1-POD1-SPINE1 | 10.4.0.10/32 |
| DC1_POD1 | DC1-POD1-SPINE2 | 10.4.0.11/32 |
| DC1_POD1 | DC1-POD1-SPINE3 | 10.4.0.12/32 |
| DC1_POD1 | DC1-POD1-SPINE4 | 10.4.0.13/32 |
| DC1_POD2 | DC1-POD2-LEAF1A | 10.4.33.22/32 |
| DC1_POD2 | DC1-POD2-LEAF1B | 10.4.33.23/32 |
| DC1_POD2 | DC1-POD2-LEAF2A | 10.4.33.24/32 |
| DC1_POD2 | DC1-POD2-LEAF2B | 10.4.33.25/32 |
| DC1_POD2 | DC1-POD2-LEAF3A | 10.4.33.26/32 |
| DC1_POD2 | DC1-POD2-LEAF3B | 10.4.33.27/32 |
| DC1_POD2 | DC1-POD2-LEAF4A | 10.4.33.28/32 |
| DC1_POD2 | DC1-POD2-LEAF4B | 10.4.33.29/32 |
| DC1_POD2 | DC1-POD2-LEAF5A | 10.4.33.30/32 |
| DC1_POD2 | DC1-POD2-LEAF5B | 10.4.33.31/32 |
| DC1_POD2 | DC1-POD2-LEAF6A | 10.4.33.32/32 |
| DC1_POD2 | DC1-POD2-LEAF6B | 10.4.33.33/32 |
| DC1_POD2 | DC1-POD2-LEAF7A | 10.4.33.34/32 |
| DC1_POD2 | DC1-POD2-LEAF7B | 10.4.33.35/32 |
| DC1_POD2 | DC1-POD2-LEAF8A | 10.4.33.36/32 |
| DC1_POD2 | DC1-POD2-LEAF8B | 10.4.33.37/32 |
| DC1_POD2 | DC1-POD2-LEAF9A | 10.4.33.38/32 |
| DC1_POD2 | DC1-POD2-LEAF9B | 10.4.33.39/32 |
| DC1_POD2 | DC1-POD2-LEAF10A | 10.4.33.40/32 |
| DC1_POD2 | DC1-POD2-LEAF10B | 10.4.33.41/32 |
| DC1_POD2 | DC1-POD2-LEAF11A | 10.4.33.42/32 |
| DC1_POD2 | DC1-POD2-LEAF11B | 10.4.33.43/32 |
| DC1_POD2 | DC1-POD2-LEAF12A | 10.4.33.44/32 |
| DC1_POD2 | DC1-POD2-LEAF12B | 10.4.33.45/32 |
| DC1_POD2 | DC1-POD2-LEAF13A | 10.4.33.46/32 |
| DC1_POD2 | DC1-POD2-LEAF13B | 10.4.33.47/32 |
| DC1_POD2 | DC1-POD2-LEAF14A | 10.4.33.48/32 |
| DC1_POD2 | DC1-POD2-LEAF14B | 10.4.33.49/32 |
| DC1_POD2 | DC1-POD2-SPINE1 | 10.4.32.10/32 |
| DC1_POD2 | DC1-POD2-SPINE2 | 10.4.32.12/32 |
| DC1_POD2 | DC1-POD2-SPINE3 | 10.4.32.3/32 |
| DC1_POD2 | DC1-POD2-SPINE4 | 10.4.32.4/32 |
| DC2_POD1 | DC2-POD1-LEAF1A | 10.4.65.22/32 |
| DC2_POD1 | DC2-POD1-LEAF1B | 10.4.65.23/32 |
| DC2_POD1 | DC2-POD1-LEAF2A | 10.4.65.25/32 |
| DC2_POD1 | DC2-POD1-LEAF2B | 10.4.65.26/32 |
| DC2_POD1 | DC2-POD1-LEAF3A | 10.4.65.27/32 |
| DC2_POD1 | DC2-POD1-LEAF3B | 10.4.65.28/32 |
| DC2_POD1 | DC2-POD1-LEAF4A | 10.4.65.29/32 |
| DC2_POD1 | DC2-POD1-LEAF4B | 10.4.65.30/32 |
| DC2_POD1 | DC2-POD1-LEAF5A | 10.4.65.31/32 |
| DC2_POD1 | DC2-POD1-LEAF5B | 10.4.65.32/32 |
| DC2_POD1 | DC2-POD1-LEAF6A | 10.4.65.33/32 |
| DC2_POD1 | DC2-POD1-LEAF6B | 10.4.65.34/32 |
| DC2_POD1 | DC2-POD1-LEAF7A | 10.4.65.35/32 |
| DC2_POD1 | DC2-POD1-LEAF7B | 10.4.65.36/32 |
| DC2_POD1 | DC2-POD1-LEAF8A | 10.4.65.37/32 |
| DC2_POD1 | DC2-POD1-LEAF8B | 10.4.65.38/32 |
| DC2_POD1 | DC2-POD1-LEAF9A | 10.4.65.39/32 |
| DC2_POD1 | DC2-POD1-LEAF9B | 10.4.65.40/32 |
| DC2_POD1 | DC2-POD1-LEAF10A | 10.4.65.41/32 |
| DC2_POD1 | DC2-POD1-LEAF10B | 10.4.65.42/32 |
| DC2_POD1 | DC2-POD1-LEAF11A | 10.4.65.43/32 |
| DC2_POD1 | DC2-POD1-LEAF11B | 10.4.65.44/32 |
| DC2_POD1 | DC2-POD1-LEAF12A | 10.4.65.45/32 |
| DC2_POD1 | DC2-POD1-LEAF12B | 10.4.65.46/32 |
| DC2_POD1 | DC2-POD1-LEAF13A | 10.4.65.47/32 |
| DC2_POD1 | DC2-POD1-LEAF13B | 10.4.65.48/32 |
| DC2_POD1 | DC2-POD1-LEAF14A | 10.4.65.49/32 |
| DC2_POD1 | DC2-POD1-LEAF14B | 10.4.65.50/32 |
| DC2_POD1 | DC2-POD1-SPINE1 | 10.4.64.10/32 |
| DC2_POD1 | DC2-POD1-SPINE2 | 10.4.64.12/32 |
| DC2_POD1 | DC2-POD1-SPINE3 | 10.4.64.13/32 |
| DC2_POD1 | DC2-POD1-SPINE4 | 10.4.64.14/32 |
| AMS | SUPER-SPINE1 | 10.4.27.10/32 |
| AMS | SUPER-SPINE2 | 10.4.27.11/32 |
| AMS | SUPER-SPINE3 | 10.4.27.12/32 |
| AMS | SUPER-SPINE4 | 10.4.27.13/32 |
| AMS | SUPER-SPINE5 | 10.4.27.14/32 |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 10.5.1.0/24 | 256 | 28 | 10.94 % |
| 10.5.33.0/24 | 256 | 28 | 10.94 % |
| 10.5.65.0/24 | 256 | 28 | 10.94 % |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DC1_POD1 | DC1-POD1-LEAF1A | 10.5.1.22/32 |
| DC1_POD1 | DC1-POD1-LEAF1B | 10.5.1.22/32 |
| DC1_POD1 | DC1-POD1-LEAF2A | 10.5.1.24/32 |
| DC1_POD1 | DC1-POD1-LEAF2B | 10.5.1.24/32 |
| DC1_POD1 | DC1-POD1-LEAF3A | 10.5.1.26/32 |
| DC1_POD1 | DC1-POD1-LEAF3B | 10.5.1.26/32 |
| DC1_POD1 | DC1-POD1-LEAF4A | 10.5.1.28/32 |
| DC1_POD1 | DC1-POD1-LEAF4B | 10.5.1.28/32 |
| DC1_POD1 | DC1-POD1-LEAF5A | 10.5.1.30/32 |
| DC1_POD1 | DC1-POD1-LEAF5B | 10.5.1.30/32 |
| DC1_POD1 | DC1-POD1-LEAF6A | 10.5.1.32/32 |
| DC1_POD1 | DC1-POD1-LEAF6B | 10.5.1.32/32 |
| DC1_POD1 | DC1-POD1-LEAF7A | 10.5.1.34/32 |
| DC1_POD1 | DC1-POD1-LEAF7B | 10.5.1.34/32 |
| DC1_POD1 | DC1-POD1-LEAF8A | 10.5.1.36/32 |
| DC1_POD1 | DC1-POD1-LEAF8B | 10.5.1.36/32 |
| DC1_POD1 | DC1-POD1-LEAF9A | 10.5.1.38/32 |
| DC1_POD1 | DC1-POD1-LEAF9B | 10.5.1.38/32 |
| DC1_POD1 | DC1-POD1-LEAF10A | 10.5.1.40/32 |
| DC1_POD1 | DC1-POD1-LEAF10B | 10.5.1.40/32 |
| DC1_POD1 | DC1-POD1-LEAF11A | 10.5.1.42/32 |
| DC1_POD1 | DC1-POD1-LEAF11B | 10.5.1.42/32 |
| DC1_POD1 | DC1-POD1-LEAF12A | 10.5.1.44/32 |
| DC1_POD1 | DC1-POD1-LEAF12B | 10.5.1.44/32 |
| DC1_POD1 | DC1-POD1-LEAF13A | 10.5.1.46/32 |
| DC1_POD1 | DC1-POD1-LEAF13B | 10.5.1.46/32 |
| DC1_POD1 | DC1-POD1-LEAF14A | 10.5.1.48/32 |
| DC1_POD1 | DC1-POD1-LEAF14B | 10.5.1.48/32 |
| DC1_POD2 | DC1-POD2-LEAF1A | 10.5.33.22/32 |
| DC1_POD2 | DC1-POD2-LEAF1B | 10.5.33.22/32 |
| DC1_POD2 | DC1-POD2-LEAF2A | 10.5.33.24/32 |
| DC1_POD2 | DC1-POD2-LEAF2B | 10.5.33.24/32 |
| DC1_POD2 | DC1-POD2-LEAF3A | 10.5.33.26/32 |
| DC1_POD2 | DC1-POD2-LEAF3B | 10.5.33.26/32 |
| DC1_POD2 | DC1-POD2-LEAF4A | 10.5.33.28/32 |
| DC1_POD2 | DC1-POD2-LEAF4B | 10.5.33.28/32 |
| DC1_POD2 | DC1-POD2-LEAF5A | 10.5.33.30/32 |
| DC1_POD2 | DC1-POD2-LEAF5B | 10.5.33.30/32 |
| DC1_POD2 | DC1-POD2-LEAF6A | 10.5.33.32/32 |
| DC1_POD2 | DC1-POD2-LEAF6B | 10.5.33.32/32 |
| DC1_POD2 | DC1-POD2-LEAF7A | 10.5.33.34/32 |
| DC1_POD2 | DC1-POD2-LEAF7B | 10.5.33.34/32 |
| DC1_POD2 | DC1-POD2-LEAF8A | 10.5.33.36/32 |
| DC1_POD2 | DC1-POD2-LEAF8B | 10.5.33.36/32 |
| DC1_POD2 | DC1-POD2-LEAF9A | 10.5.33.38/32 |
| DC1_POD2 | DC1-POD2-LEAF9B | 10.5.33.38/32 |
| DC1_POD2 | DC1-POD2-LEAF10A | 10.5.33.40/32 |
| DC1_POD2 | DC1-POD2-LEAF10B | 10.5.33.40/32 |
| DC1_POD2 | DC1-POD2-LEAF11A | 10.5.33.42/32 |
| DC1_POD2 | DC1-POD2-LEAF11B | 10.5.33.42/32 |
| DC1_POD2 | DC1-POD2-LEAF12A | 10.5.33.44/32 |
| DC1_POD2 | DC1-POD2-LEAF12B | 10.5.33.44/32 |
| DC1_POD2 | DC1-POD2-LEAF13A | 10.5.33.46/32 |
| DC1_POD2 | DC1-POD2-LEAF13B | 10.5.33.46/32 |
| DC1_POD2 | DC1-POD2-LEAF14A | 10.5.33.48/32 |
| DC1_POD2 | DC1-POD2-LEAF14B | 10.5.33.48/32 |
| DC2_POD1 | DC2-POD1-LEAF1A | 10.5.65.22/32 |
| DC2_POD1 | DC2-POD1-LEAF1B | 10.5.65.22/32 |
| DC2_POD1 | DC2-POD1-LEAF2A | 10.5.65.25/32 |
| DC2_POD1 | DC2-POD1-LEAF2B | 10.5.65.25/32 |
| DC2_POD1 | DC2-POD1-LEAF3A | 10.5.65.27/32 |
| DC2_POD1 | DC2-POD1-LEAF3B | 10.5.65.27/32 |
| DC2_POD1 | DC2-POD1-LEAF4A | 10.5.65.29/32 |
| DC2_POD1 | DC2-POD1-LEAF4B | 10.5.65.29/32 |
| DC2_POD1 | DC2-POD1-LEAF5A | 10.5.65.31/32 |
| DC2_POD1 | DC2-POD1-LEAF5B | 10.5.65.31/32 |
| DC2_POD1 | DC2-POD1-LEAF6A | 10.5.65.33/32 |
| DC2_POD1 | DC2-POD1-LEAF6B | 10.5.65.33/32 |
| DC2_POD1 | DC2-POD1-LEAF7A | 10.5.65.35/32 |
| DC2_POD1 | DC2-POD1-LEAF7B | 10.5.65.35/32 |
| DC2_POD1 | DC2-POD1-LEAF8A | 10.5.65.37/32 |
| DC2_POD1 | DC2-POD1-LEAF8B | 10.5.65.37/32 |
| DC2_POD1 | DC2-POD1-LEAF9A | 10.5.65.39/32 |
| DC2_POD1 | DC2-POD1-LEAF9B | 10.5.65.39/32 |
| DC2_POD1 | DC2-POD1-LEAF10A | 10.5.65.41/32 |
| DC2_POD1 | DC2-POD1-LEAF10B | 10.5.65.41/32 |
| DC2_POD1 | DC2-POD1-LEAF11A | 10.5.65.43/32 |
| DC2_POD1 | DC2-POD1-LEAF11B | 10.5.65.43/32 |
| DC2_POD1 | DC2-POD1-LEAF12A | 10.5.65.45/32 |
| DC2_POD1 | DC2-POD1-LEAF12B | 10.5.65.45/32 |
| DC2_POD1 | DC2-POD1-LEAF13A | 10.5.65.47/32 |
| DC2_POD1 | DC2-POD1-LEAF13B | 10.5.65.47/32 |
| DC2_POD1 | DC2-POD1-LEAF14A | 10.5.65.49/32 |
| DC2_POD1 | DC2-POD1-LEAF14B | 10.5.65.49/32 |

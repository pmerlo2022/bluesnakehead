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
| DC1_POD1 | l3leaf | DC1-POD1-LEAF1A | 192.168.1.7/24 Test without management IP | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF1B | 192.168.1.8/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF2A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF2B | 192.168.1.9/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF3A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF3B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF4A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF4B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF5A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF5B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF6A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF6B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF7A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF7B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF8A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF8B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF9A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF9B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF10A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF10B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF11A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF11B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF12A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF12B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF13A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF13B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF14A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF14B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE1 | - | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE2 | - | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE3 | - | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE4 | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF1A | 192.168.1.7/24 Test without management IP | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF1B | 192.168.1.8/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF2A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF2B | 192.168.1.9/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF3A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF3B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF4A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF4B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF5A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF5B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF6A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF6B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF7A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF7B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF8A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF8B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF9A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF9B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF10A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF10B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF11A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF11B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF12A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF12B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF13A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF13B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF14A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF14B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE1 | 192.168.1.13/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE2 | 192.168.1.14/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE3 | 192.168.1.15/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE4 | 192.168.1.16/24 | vEOS-LAB | Provisioned |
| DC1 | super-spine | DC1-SUPER-SPINE1 | 10.6.0.1/24 | vEOS-LAB | Provisioned |
| DC1 | super-spine | DC1-SUPER-SPINE2 | 10.6.0.2/24 | vEOS-LAB | Provisioned |
| DC1 | super-spine | DC1-SUPER-SPINE3 | 10.6.0.3/24 | vEOS-LAB | Provisioned |
| DC1 | super-spine | DC1-SUPER-SPINE4 | 10.6.0.4/24 | vEOS-LAB | Provisioned |
| DC1 | super-spine | DC1-SUPER-SPINE5 | 10.6.0.5/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF1A | 192.168.1.7/24 Test without management IP | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF1B | 192.168.1.8/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF2A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF2B | 192.168.1.9/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF3A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF3B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF4A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF4B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF5A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF5B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF6A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF6B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF7A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF7B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF8A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF8B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF9A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF9B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF10A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF10B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF11A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF11B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF12A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF12B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF13A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF13B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF14A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF14B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE1 | 192.168.1.20/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE2 | 192.168.1.21/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE3 | 192.168.1.22/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE4 | 10.6.32.4/24 | vEOS-LAB | Provisioned |
| DC2 | super-spine | DC2-SUPER-SPINE1 | 10.6.64.1/24 | vEOS-LAB | Provisioned |
| DC2 | super-spine | DC2-SUPER-SPINE2 | 10.6.64.2/24 | vEOS-LAB | Provisioned |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | DC1-POD1-LEAF1A | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet6 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet5 | mlag_peer | DC1-POD1-LEAF1B | Ethernet5 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet6 | l3leaf | DC1-POD1-LEAF1B | Ethernet4 |
| l3leaf | DC1-POD1-LEAF1B | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF1B | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF1B | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet6 |
| l3leaf | DC1-POD1-LEAF1B | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF2A | Ethernet1 | spine | DC1-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF2A | Ethernet2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF2A | Ethernet5 | mlag_peer | DC1-POD1-LEAF2B | Ethernet5 |
| l3leaf | DC1-POD1-LEAF2A | Ethernet6 | mlag_peer | DC1-POD1-LEAF2B | Ethernet6 |
| l3leaf | DC1-POD1-LEAF2A | Ethernet11 | spine | DC1-POD1-SPINE3 | Ethernet6 |
| l3leaf | DC1-POD1-LEAF2A | Ethernet12 | spine | DC1-POD1-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet1 | spine | DC1-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet11 | spine | DC1-POD1-SPINE3 | Ethernet6 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet12 | spine | DC1-POD1-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF5A | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF5A | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF5A | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF5A | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF5B | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF5B | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF5B | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF5B | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF6A | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF6A | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF6A | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF6A | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF6A | Ethernet5 | mlag_peer | DC1-POD1-LEAF6B | Ethernet5 |
| l3leaf | DC1-POD1-LEAF6A | Ethernet6 | mlag_peer | DC1-POD1-LEAF6B | Ethernet6 |
| l3leaf | DC1-POD1-LEAF6B | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF6B | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF6B | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF6B | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF7A | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF7A | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF7A | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF7A | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF7A | Ethernet5 | mlag_peer | DC1-POD1-LEAF7B | Ethernet5 |
| l3leaf | DC1-POD1-LEAF7A | Ethernet6 | mlag_peer | DC1-POD1-LEAF7B | Ethernet6 |
| l3leaf | DC1-POD1-LEAF7B | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF7B | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF7B | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF7B | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF8A | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF8A | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF8A | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF8A | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF8A | Ethernet5 | mlag_peer | DC1-POD1-LEAF8B | Ethernet5 |
| l3leaf | DC1-POD1-LEAF8A | Ethernet6 | mlag_peer | DC1-POD1-LEAF8B | Ethernet6 |
| l3leaf | DC1-POD1-LEAF8B | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF8B | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF8B | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF8B | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF9A | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF9A | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF9A | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF9A | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF9A | Ethernet5 | mlag_peer | DC1-POD1-LEAF9B | Ethernet5 |
| l3leaf | DC1-POD1-LEAF9A | Ethernet6 | mlag_peer | DC1-POD1-LEAF9B | Ethernet6 |
| l3leaf | DC1-POD1-LEAF9B | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF9B | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF9B | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF9B | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF10A | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF10A | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF10A | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF10A | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF10A | Ethernet5 | mlag_peer | DC1-POD1-LEAF10B | Ethernet5 |
| l3leaf | DC1-POD1-LEAF10A | Ethernet6 | mlag_peer | DC1-POD1-LEAF10B | Ethernet6 |
| l3leaf | DC1-POD1-LEAF10B | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF10B | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF10B | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF10B | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF11A | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF11A | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF11A | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF11A | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF11A | Ethernet5 | mlag_peer | DC1-POD1-LEAF11B | Ethernet5 |
| l3leaf | DC1-POD1-LEAF11A | Ethernet6 | mlag_peer | DC1-POD1-LEAF11B | Ethernet6 |
| l3leaf | DC1-POD1-LEAF11B | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF11B | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF11B | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF11B | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF12A | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF12A | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF12A | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF12A | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF12A | Ethernet5 | mlag_peer | DC1-POD1-LEAF12B | Ethernet5 |
| l3leaf | DC1-POD1-LEAF12A | Ethernet6 | mlag_peer | DC1-POD1-LEAF12B | Ethernet6 |
| l3leaf | DC1-POD1-LEAF12B | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF12B | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF12B | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF12B | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF13A | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF13A | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF13A | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF13A | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF13A | Ethernet5 | mlag_peer | DC1-POD1-LEAF13B | Ethernet5 |
| l3leaf | DC1-POD1-LEAF13A | Ethernet6 | mlag_peer | DC1-POD1-LEAF13B | Ethernet6 |
| l3leaf | DC1-POD1-LEAF13B | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF13B | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF13B | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF13B | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF14A | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF14A | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF14A | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF14A | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF14A | Ethernet5 | mlag_peer | DC1-POD1-LEAF14B | Ethernet5 |
| l3leaf | DC1-POD1-LEAF14A | Ethernet6 | mlag_peer | DC1-POD1-LEAF14B | Ethernet6 |
| l3leaf | DC1-POD1-LEAF14B | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF14B | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF14B | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF14B | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet8 |
| spine | DC1-POD1-SPINE1 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet17/1 |
| spine | DC1-POD1-SPINE1 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet17/2 |
| spine | DC1-POD1-SPINE1 | Ethernet3 | super-spine | DC1-SUPER-SPINE3 | Ethernet17/3 |
| spine | DC1-POD1-SPINE1 | Ethernet4 | l3leaf | DC2-POD1-LEAF14A | Ethernet1/1 |
| spine | DC1-POD1-SPINE1 | Ethernet5 | l3leaf | DC2-POD1-LEAF14B | Ethernet1/1 |
| spine | DC1-POD1-SPINE2 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet17/1 |
| spine | DC1-POD1-SPINE2 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet17/2 |
| spine | DC1-POD1-SPINE2 | Ethernet3 | super-spine | DC1-SUPER-SPINE3 | Ethernet17/3 |
| spine | DC1-POD1-SPINE2 | Ethernet4 | l3leaf | DC2-POD1-LEAF14A | Ethernet1/2 |
| spine | DC1-POD1-SPINE2 | Ethernet5 | l3leaf | DC2-POD1-LEAF14B | Ethernet1/2 |
| spine | DC1-POD1-SPINE3 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet17/1 |
| spine | DC1-POD1-SPINE3 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet17/2 |
| spine | DC1-POD1-SPINE3 | Ethernet3 | super-spine | DC1-SUPER-SPINE3 | Ethernet17/3 |
| spine | DC1-POD1-SPINE3 | Ethernet4 | super-spine | DC1-SUPER-SPINE4 | Ethernet17/4 |
| spine | DC1-POD1-SPINE3 | Ethernet6 | l3leaf | DC2-POD1-LEAF2B | Ethernet1/3 |
| spine | DC1-POD1-SPINE3 | Ethernet7 | l3leaf | DC2-POD1-LEAF14A | Ethernet1/3 |
| spine | DC1-POD1-SPINE3 | Ethernet8 | l3leaf | DC2-POD1-LEAF14B | Ethernet1/3 |
| spine | DC1-POD1-SPINE4 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet17/1 |
| spine | DC1-POD1-SPINE4 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet17/2 |
| spine | DC1-POD1-SPINE4 | Ethernet3 | super-spine | DC1-SUPER-SPINE3 | Ethernet17/3 |
| spine | DC1-POD1-SPINE4 | Ethernet4 | super-spine | DC1-SUPER-SPINE4 | Ethernet17/4 |
| spine | DC1-POD1-SPINE4 | Ethernet7 | l3leaf | DC2-POD1-LEAF14A | Ethernet1/4 |
| spine | DC1-POD1-SPINE4 | Ethernet8 | l3leaf | DC2-POD1-LEAF14B | Ethernet1/4 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet6 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet5 | mlag_peer | DC1-POD2-LEAF1B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF1B | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF1B | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF1B | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet6 |
| l3leaf | DC1-POD2-LEAF1B | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF1B | Ethernet6 | mlag_peer | DC1-POD2-LEAF1A | Ethernet6 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet6 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet5 | mlag_peer | DC1-POD2-LEAF2B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet6 | mlag_peer | DC1-POD2-LEAF2B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF2B | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF2B | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF2B | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet6 |
| l3leaf | DC1-POD2-LEAF2B | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet5 | mlag_peer | DC1-POD2-LEAF3B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet6 | mlag_peer | DC1-POD2-LEAF3B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF3B | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF3B | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF3B | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF3B | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet5 | mlag_peer | DC1-POD2-LEAF4B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet6 | mlag_peer | DC1-POD2-LEAF4B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF4B | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF4B | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF4B | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF4B | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet5 | mlag_peer | DC1-POD2-LEAF5B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet6 | mlag_peer | DC1-POD2-LEAF5B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF5B | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF5B | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF5B | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF5B | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet5 | mlag_peer | DC1-POD2-LEAF6B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet6 | mlag_peer | DC1-POD2-LEAF6B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF6B | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF6B | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF6B | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF6B | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet5 | mlag_peer | DC1-POD2-LEAF7B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet6 | mlag_peer | DC1-POD2-LEAF7B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF7B | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF7B | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF7B | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF7B | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet5 | mlag_peer | DC1-POD2-LEAF8B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet6 | mlag_peer | DC1-POD2-LEAF8B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF8B | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF8B | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF8B | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF8B | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet5 | mlag_peer | DC1-POD2-LEAF9B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet6 | mlag_peer | DC1-POD2-LEAF9B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF9B | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF9B | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF9B | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF9B | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet5 | mlag_peer | DC1-POD2-LEAF10B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet6 | mlag_peer | DC1-POD2-LEAF10B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF10B | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF10B | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF10B | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF10B | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet5 | mlag_peer | DC1-POD2-LEAF11B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet6 | mlag_peer | DC1-POD2-LEAF11B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF11B | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF11B | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF11B | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF11B | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet5 | mlag_peer | DC1-POD2-LEAF12B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet6 | mlag_peer | DC1-POD2-LEAF12B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF12B | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF12B | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF12B | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF12B | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet5 | mlag_peer | DC1-POD2-LEAF13B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet6 | mlag_peer | DC1-POD2-LEAF13B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF13B | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF13B | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF13B | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF13B | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet5 | mlag_peer | DC1-POD2-LEAF14B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet6 | mlag_peer | DC1-POD2-LEAF14B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF14B | Ethernet1/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF14B | Ethernet1/2 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF14B | Ethernet1/3 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF14B | Ethernet1/4 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| spine | DC1-POD2-SPINE1 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet1 |
| spine | DC1-POD2-SPINE1 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet2 |
| spine | DC1-POD2-SPINE1 | Ethernet3 | super-spine | DC1-SUPER-SPINE3 | Ethernet3 |
| spine | DC1-POD2-SPINE2 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet1 |
| spine | DC1-POD2-SPINE2 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet2 |
| spine | DC1-POD2-SPINE2 | Ethernet3 | super-spine | DC1-SUPER-SPINE3 | Ethernet3 |
| spine | DC1-POD2-SPINE3 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet17/1 |
| spine | DC1-POD2-SPINE3 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet17/2 |
| spine | DC1-POD2-SPINE3 | Ethernet3 | super-spine | DC1-SUPER-SPINE3 | Ethernet17/3 |
| spine | DC1-POD2-SPINE3 | Ethernet4 | super-spine | DC1-SUPER-SPINE4 | Ethernet17/4 |
| spine | DC1-POD2-SPINE4 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet17/1 |
| spine | DC1-POD2-SPINE4 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet17/2 |
| spine | DC1-POD2-SPINE4 | Ethernet3 | super-spine | DC1-SUPER-SPINE3 | Ethernet17/3 |
| spine | DC1-POD2-SPINE4 | Ethernet4 | super-spine | DC1-SUPER-SPINE4 | Ethernet17/4 |
| super-spine | DC1-SUPER-SPINE1 | Ethernet1 | spine | DC2-POD1-SPINE4 | Ethernet1 |
| super-spine | DC1-SUPER-SPINE2 | Ethernet2 | spine | DC2-POD1-SPINE4 | Ethernet2 |
| super-spine | DC1-SUPER-SPINE3 | Ethernet3 | spine | DC2-POD1-SPINE4 | Ethernet3 |
| super-spine | DC1-SUPER-SPINE4 | Ethernet4 | spine | DC2-POD1-SPINE4 | Ethernet4 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet5 | l3leaf | DC2-POD1-LEAF1B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet6 | mlag_peer | DC2-POD1-LEAF1B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF2A | Ethernet5 | mlag_peer | DC2-POD1-LEAF2B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF2A | Ethernet6 | mlag_peer | DC2-POD1-LEAF2B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF3A | Ethernet5 | mlag_peer | DC2-POD1-LEAF3B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF3A | Ethernet6 | mlag_peer | DC2-POD1-LEAF3B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF4A | Ethernet5 | mlag_peer | DC2-POD1-LEAF4B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF4A | Ethernet6 | mlag_peer | DC2-POD1-LEAF4B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF5A | Ethernet5 | mlag_peer | DC2-POD1-LEAF5B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF5A | Ethernet6 | mlag_peer | DC2-POD1-LEAF5B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF6A | Ethernet5 | mlag_peer | DC2-POD1-LEAF6B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF6A | Ethernet6 | mlag_peer | DC2-POD1-LEAF6B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF7A | Ethernet5 | mlag_peer | DC2-POD1-LEAF7B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF7A | Ethernet6 | mlag_peer | DC2-POD1-LEAF7B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF8A | Ethernet5 | mlag_peer | DC2-POD1-LEAF8B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF8A | Ethernet6 | mlag_peer | DC2-POD1-LEAF8B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF9A | Ethernet5 | mlag_peer | DC2-POD1-LEAF9B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF9A | Ethernet6 | mlag_peer | DC2-POD1-LEAF9B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF10A | Ethernet5 | mlag_peer | DC2-POD1-LEAF10B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF10A | Ethernet6 | mlag_peer | DC2-POD1-LEAF10B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF11A | Ethernet5 | mlag_peer | DC2-POD1-LEAF11B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF11A | Ethernet6 | mlag_peer | DC2-POD1-LEAF11B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF12A | Ethernet5 | mlag_peer | DC2-POD1-LEAF12B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF12A | Ethernet6 | mlag_peer | DC2-POD1-LEAF12B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF13A | Ethernet5 | mlag_peer | DC2-POD1-LEAF13B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF13A | Ethernet6 | mlag_peer | DC2-POD1-LEAF13B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF14A | Ethernet5 | mlag_peer | DC2-POD1-LEAF14B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF14A | Ethernet6 | mlag_peer | DC2-POD1-LEAF14B | Ethernet6 |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 172.16.1.0/24 | 256 | 14 | 5.47 % |
| 172.16.2.0/24 | 256 | 36 | 14.07 % |
| 172.16.32.0/24 | 256 | 14 | 5.47 % |
| 172.17.1.0/24 | 256 | 112 | 43.75 % |
| 172.17.2.0/24 | 256 | 224 | 87.5 % |
| 172.17.32.0/24 | 256 | 130 | 50.79 % |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| DC1-POD1-LEAF1A | Ethernet1/1 | 172.17.1.1/31 | DC1-POD1-SPINE1 | Ethernet4 | 172.17.32.16/31 |
| DC1-POD1-LEAF1A | Ethernet1/2 | 172.17.1.3/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.32.26/31 |
| DC1-POD1-LEAF1A | Ethernet1/3 | 172.17.1.5/31 | DC1-POD1-SPINE3 | Ethernet6 | 172.17.32.28/31 |
| DC1-POD1-LEAF1A | Ethernet1/4 | 172.17.1.7/31 | DC1-POD1-SPINE4 | Ethernet7 | 172.17.32.22/31 |
| DC1-POD1-LEAF1A | Ethernet6 | 11.1.0.0/31 | DC1-POD1-LEAF1B | Ethernet4 | 11.1.0.1/31 |
| DC1-POD1-LEAF1B | Ethernet1/1 | 172.17.1.9/31 | DC1-POD1-SPINE1 | Ethernet4 | 172.17.32.16/31 |
| DC1-POD1-LEAF1B | Ethernet1/2 | 172.17.1.11/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.32.26/31 |
| DC1-POD1-LEAF1B | Ethernet1/3 | 172.17.1.13/31 | DC1-POD1-SPINE3 | Ethernet6 | 172.17.32.28/31 |
| DC1-POD1-LEAF1B | Ethernet1/4 | 172.17.1.15/31 | DC1-POD1-SPINE4 | Ethernet7 | 172.17.32.22/31 |
| DC1-POD1-LEAF2A | Ethernet1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet4 | 172.17.32.16/31 |
| DC1-POD1-LEAF2A | Ethernet2 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.32.26/31 |
| DC1-POD1-LEAF2A | Ethernet11 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet6 | 172.17.32.28/31 |
| DC1-POD1-LEAF2A | Ethernet12 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet7 | 172.17.32.22/31 |
| DC1-POD1-LEAF2B | Ethernet1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet4 | 172.17.32.16/31 |
| DC1-POD1-LEAF2B | Ethernet2 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.32.26/31 |
| DC1-POD1-LEAF2B | Ethernet11 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet6 | 172.17.32.28/31 |
| DC1-POD1-LEAF2B | Ethernet12 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet7 | 172.17.32.22/31 |
| DC1-POD1-LEAF3A | Ethernet1/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet4 | 172.17.32.16/31 |
| DC1-POD1-LEAF3A | Ethernet1/2 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet4 | 172.17.32.18/31 |
| DC1-POD1-LEAF3A | Ethernet1/3 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet7 | 172.17.32.20/31 |
| DC1-POD1-LEAF3A | Ethernet1/4 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet7 | 172.17.32.22/31 |
| DC1-POD1-LEAF3B | Ethernet1/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet5 | 172.17.32.24/31 |
| DC1-POD1-LEAF3B | Ethernet1/2 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.32.26/31 |
| DC1-POD1-LEAF3B | Ethernet1/3 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet8 | 172.17.32.28/31 |
| DC1-POD1-LEAF3B | Ethernet1/4 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet8 | 172.17.32.30/31 |
| DC1-POD1-LEAF4A | Ethernet1/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet4 | 172.17.32.16/31 |
| DC1-POD1-LEAF4A | Ethernet1/2 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet4 | 172.17.32.18/31 |
| DC1-POD1-LEAF4A | Ethernet1/3 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet7 | 172.17.32.20/31 |
| DC1-POD1-LEAF4A | Ethernet1/4 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet7 | 172.17.32.22/31 |
| DC1-POD1-LEAF4B | Ethernet1/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet5 | 172.17.32.24/31 |
| DC1-POD1-LEAF4B | Ethernet1/2 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.32.26/31 |
| DC1-POD1-LEAF4B | Ethernet1/3 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet8 | 172.17.32.28/31 |
| DC1-POD1-LEAF4B | Ethernet1/4 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet8 | 172.17.32.30/31 |
| DC1-POD1-LEAF5A | Ethernet1/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet4 | 172.17.32.16/31 |
| DC1-POD1-LEAF5A | Ethernet1/2 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet4 | 172.17.32.18/31 |
| DC1-POD1-LEAF5A | Ethernet1/3 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet7 | 172.17.32.20/31 |
| DC1-POD1-LEAF5A | Ethernet1/4 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet7 | 172.17.32.22/31 |
| DC1-POD1-LEAF5B | Ethernet1/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet5 | 172.17.32.24/31 |
| DC1-POD1-LEAF5B | Ethernet1/2 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.32.26/31 |
| DC1-POD1-LEAF5B | Ethernet1/3 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet8 | 172.17.32.28/31 |
| DC1-POD1-LEAF5B | Ethernet1/4 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet8 | 172.17.32.30/31 |
| DC1-POD1-LEAF6A | Ethernet1/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet4 | 172.17.32.16/31 |
| DC1-POD1-LEAF6A | Ethernet1/2 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet4 | 172.17.32.18/31 |
| DC1-POD1-LEAF6A | Ethernet1/3 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet7 | 172.17.32.20/31 |
| DC1-POD1-LEAF6A | Ethernet1/4 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet7 | 172.17.32.22/31 |
| DC1-POD1-LEAF6B | Ethernet1/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet5 | 172.17.32.24/31 |
| DC1-POD1-LEAF6B | Ethernet1/2 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.32.26/31 |
| DC1-POD1-LEAF6B | Ethernet1/3 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet8 | 172.17.32.28/31 |
| DC1-POD1-LEAF6B | Ethernet1/4 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet8 | 172.17.32.30/31 |
| DC1-POD1-LEAF7A | Ethernet1/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet4 | 172.17.32.16/31 |
| DC1-POD1-LEAF7A | Ethernet1/2 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet4 | 172.17.32.18/31 |
| DC1-POD1-LEAF7A | Ethernet1/3 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet7 | 172.17.32.20/31 |
| DC1-POD1-LEAF7A | Ethernet1/4 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet7 | 172.17.32.22/31 |
| DC1-POD1-LEAF7B | Ethernet1/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet5 | 172.17.32.24/31 |
| DC1-POD1-LEAF7B | Ethernet1/2 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.32.26/31 |
| DC1-POD1-LEAF7B | Ethernet1/3 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet8 | 172.17.32.28/31 |
| DC1-POD1-LEAF7B | Ethernet1/4 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet8 | 172.17.32.30/31 |
| DC1-POD1-LEAF8A | Ethernet1/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet4 | 172.17.32.16/31 |
| DC1-POD1-LEAF8A | Ethernet1/2 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet4 | 172.17.32.18/31 |
| DC1-POD1-LEAF8A | Ethernet1/3 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet7 | 172.17.32.20/31 |
| DC1-POD1-LEAF8A | Ethernet1/4 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet7 | 172.17.32.22/31 |
| DC1-POD1-LEAF8B | Ethernet1/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet5 | 172.17.32.24/31 |
| DC1-POD1-LEAF8B | Ethernet1/2 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.32.26/31 |
| DC1-POD1-LEAF8B | Ethernet1/3 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet8 | 172.17.32.28/31 |
| DC1-POD1-LEAF8B | Ethernet1/4 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet8 | 172.17.32.30/31 |
| DC1-POD1-LEAF9A | Ethernet1/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet4 | 172.17.32.16/31 |
| DC1-POD1-LEAF9A | Ethernet1/2 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet4 | 172.17.32.18/31 |
| DC1-POD1-LEAF9A | Ethernet1/3 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet7 | 172.17.32.20/31 |
| DC1-POD1-LEAF9A | Ethernet1/4 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet7 | 172.17.32.22/31 |
| DC1-POD1-LEAF9B | Ethernet1/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet5 | 172.17.32.24/31 |
| DC1-POD1-LEAF9B | Ethernet1/2 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.32.26/31 |
| DC1-POD1-LEAF9B | Ethernet1/3 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet8 | 172.17.32.28/31 |
| DC1-POD1-LEAF9B | Ethernet1/4 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet8 | 172.17.32.30/31 |
| DC1-POD1-LEAF10A | Ethernet1/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet4 | 172.17.32.16/31 |
| DC1-POD1-LEAF10A | Ethernet1/2 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet4 | 172.17.32.18/31 |
| DC1-POD1-LEAF10A | Ethernet1/3 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet7 | 172.17.32.20/31 |
| DC1-POD1-LEAF10A | Ethernet1/4 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet7 | 172.17.32.22/31 |
| DC1-POD1-LEAF10B | Ethernet1/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet5 | 172.17.32.24/31 |
| DC1-POD1-LEAF10B | Ethernet1/2 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.32.26/31 |
| DC1-POD1-LEAF10B | Ethernet1/3 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet8 | 172.17.32.28/31 |
| DC1-POD1-LEAF10B | Ethernet1/4 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet8 | 172.17.32.30/31 |
| DC1-POD1-LEAF11A | Ethernet1/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet4 | 172.17.32.16/31 |
| DC1-POD1-LEAF11A | Ethernet1/2 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet4 | 172.17.32.18/31 |
| DC1-POD1-LEAF11A | Ethernet1/3 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet7 | 172.17.32.20/31 |
| DC1-POD1-LEAF11A | Ethernet1/4 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet7 | 172.17.32.22/31 |
| DC1-POD1-LEAF11B | Ethernet1/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet5 | 172.17.32.24/31 |
| DC1-POD1-LEAF11B | Ethernet1/2 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.32.26/31 |
| DC1-POD1-LEAF11B | Ethernet1/3 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet8 | 172.17.32.28/31 |
| DC1-POD1-LEAF11B | Ethernet1/4 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet8 | 172.17.32.30/31 |
| DC1-POD1-LEAF12A | Ethernet1/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet4 | 172.17.32.16/31 |
| DC1-POD1-LEAF12A | Ethernet1/2 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet4 | 172.17.32.18/31 |
| DC1-POD1-LEAF12A | Ethernet1/3 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet7 | 172.17.32.20/31 |
| DC1-POD1-LEAF12A | Ethernet1/4 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet7 | 172.17.32.22/31 |
| DC1-POD1-LEAF12B | Ethernet1/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet5 | 172.17.32.24/31 |
| DC1-POD1-LEAF12B | Ethernet1/2 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.32.26/31 |
| DC1-POD1-LEAF12B | Ethernet1/3 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet8 | 172.17.32.28/31 |
| DC1-POD1-LEAF12B | Ethernet1/4 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet8 | 172.17.32.30/31 |
| DC1-POD1-LEAF13A | Ethernet1/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet4 | 172.17.32.16/31 |
| DC1-POD1-LEAF13A | Ethernet1/2 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet4 | 172.17.32.18/31 |
| DC1-POD1-LEAF13A | Ethernet1/3 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet7 | 172.17.32.20/31 |
| DC1-POD1-LEAF13A | Ethernet1/4 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet7 | 172.17.32.22/31 |
| DC1-POD1-LEAF13B | Ethernet1/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet5 | 172.17.32.24/31 |
| DC1-POD1-LEAF13B | Ethernet1/2 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.32.26/31 |
| DC1-POD1-LEAF13B | Ethernet1/3 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet8 | 172.17.32.28/31 |
| DC1-POD1-LEAF13B | Ethernet1/4 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet8 | 172.17.32.30/31 |
| DC1-POD1-LEAF14A | Ethernet1/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet4 | 172.17.32.16/31 |
| DC1-POD1-LEAF14A | Ethernet1/2 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet4 | 172.17.32.18/31 |
| DC1-POD1-LEAF14A | Ethernet1/3 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet7 | 172.17.32.20/31 |
| DC1-POD1-LEAF14A | Ethernet1/4 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet7 | 172.17.32.22/31 |
| DC1-POD1-LEAF14B | Ethernet1/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet5 | 172.17.32.24/31 |
| DC1-POD1-LEAF14B | Ethernet1/2 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.32.26/31 |
| DC1-POD1-LEAF14B | Ethernet1/3 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet8 | 172.17.32.28/31 |
| DC1-POD1-LEAF14B | Ethernet1/4 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet8 | 172.17.32.30/31 |
| DC1-POD1-SPINE1 | Ethernet1 | 172.16.1.1/31 | DC1-SUPER-SPINE1 | Ethernet17/1 | 172.16.2.6/31 |
| DC1-POD1-SPINE1 | Ethernet2 | 172.16.1.65/31 | DC1-SUPER-SPINE2 | Ethernet17/2 | 172.16.2.70/31 |
| DC1-POD1-SPINE1 | Ethernet3 | 172.16.1.129/31 | DC1-SUPER-SPINE3 | Ethernet17/3 | 172.16.2.134/31 |
| DC1-POD1-SPINE1 | Ethernet4 | 172.17.32.16/31 | DC2-POD1-LEAF14A | Ethernet1/1 | 172.17.32.17/31 |
| DC1-POD1-SPINE1 | Ethernet5 | 172.17.32.24/31 | DC2-POD1-LEAF14B | Ethernet1/1 | 172.17.32.25/31 |
| DC1-POD1-SPINE2 | Ethernet1 | 172.16.1.3/31 | DC1-SUPER-SPINE1 | Ethernet17/1 | 172.16.2.6/31 |
| DC1-POD1-SPINE2 | Ethernet2 | 172.16.1.67/31 | DC1-SUPER-SPINE2 | Ethernet17/2 | 172.16.2.70/31 |
| DC1-POD1-SPINE2 | Ethernet3 | 172.16.1.131/31 | DC1-SUPER-SPINE3 | Ethernet17/3 | 172.16.2.134/31 |
| DC1-POD1-SPINE2 | Ethernet4 | 172.17.32.18/31 | DC2-POD1-LEAF14A | Ethernet1/2 | 172.17.32.19/31 |
| DC1-POD1-SPINE2 | Ethernet5 | 172.17.32.26/31 | DC2-POD1-LEAF14B | Ethernet1/2 | 172.17.32.27/31 |
| DC1-POD1-SPINE3 | Ethernet1 | 172.16.1.5/31 | DC1-SUPER-SPINE1 | Ethernet17/1 | 172.16.2.6/31 |
| DC1-POD1-SPINE3 | Ethernet2 | 172.16.1.69/31 | DC1-SUPER-SPINE2 | Ethernet17/2 | 172.16.2.70/31 |
| DC1-POD1-SPINE3 | Ethernet3 | 172.16.1.133/31 | DC1-SUPER-SPINE3 | Ethernet17/3 | 172.16.2.134/31 |
| DC1-POD1-SPINE3 | Ethernet4 | 172.16.1.197/31 | DC1-SUPER-SPINE4 | Ethernet17/4 | 172.16.2.198/31 |
| DC1-POD1-SPINE3 | Ethernet6 | 172.17.32.28/31 | DC2-POD1-LEAF2B | Ethernet1/3 | 172.17.32.29/31 |
| DC1-POD1-SPINE3 | Ethernet7 | 172.17.32.20/31 | DC2-POD1-LEAF14A | Ethernet1/3 | 172.17.32.21/31 |
| DC1-POD1-SPINE3 | Ethernet8 | 172.17.32.28/31 | DC2-POD1-LEAF14B | Ethernet1/3 | 172.17.32.29/31 |
| DC1-POD1-SPINE4 | Ethernet1 | 172.16.1.7/31 | DC1-SUPER-SPINE1 | Ethernet17/1 | 172.16.2.6/31 |
| DC1-POD1-SPINE4 | Ethernet2 | 172.16.1.71/31 | DC1-SUPER-SPINE2 | Ethernet17/2 | 172.16.2.70/31 |
| DC1-POD1-SPINE4 | Ethernet3 | 172.16.1.135/31 | DC1-SUPER-SPINE3 | Ethernet17/3 | 172.16.2.134/31 |
| DC1-POD1-SPINE4 | Ethernet4 | 172.16.1.199/31 | DC1-SUPER-SPINE4 | Ethernet17/4 | 172.16.2.198/31 |
| DC1-POD1-SPINE4 | Ethernet7 | 172.17.32.22/31 | DC2-POD1-LEAF14A | Ethernet1/4 | 172.17.32.23/31 |
| DC1-POD1-SPINE4 | Ethernet8 | 172.17.32.30/31 | DC2-POD1-LEAF14B | Ethernet1/4 | 172.17.32.31/31 |
| DC1-POD2-LEAF1A | Ethernet1/1 | 172.17.2.1/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF1A | Ethernet1/2 | 172.17.2.3/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF1A | Ethernet1/3 | 172.17.2.5/31 | DC1-POD2-SPINE3 | Ethernet6 | 172.17.2.28/31 |
| DC1-POD2-LEAF1A | Ethernet1/4 | 172.17.2.7/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF1B | Ethernet1/1 | 172.17.2.9/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF1B | Ethernet1/2 | 172.17.2.11/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF1B | Ethernet1/3 | 172.17.2.13/31 | DC1-POD2-SPINE3 | Ethernet6 | 172.17.2.28/31 |
| DC1-POD2-LEAF1B | Ethernet1/4 | 172.17.2.15/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF2A | Ethernet1/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF2A | Ethernet1/2 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF2A | Ethernet1/3 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet6 | 172.17.2.28/31 |
| DC1-POD2-LEAF2A | Ethernet1/4 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF2B | Ethernet1/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF2B | Ethernet1/2 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF2B | Ethernet1/3 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet6 | 172.17.2.28/31 |
| DC1-POD2-LEAF2B | Ethernet1/4 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF3A | Ethernet1/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF3A | Ethernet1/2 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF3A | Ethernet1/3 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF3A | Ethernet1/4 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF3B | Ethernet1/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF3B | Ethernet1/2 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF3B | Ethernet1/3 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF3B | Ethernet1/4 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF4A | Ethernet1/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF4A | Ethernet1/2 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF4A | Ethernet1/3 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF4A | Ethernet1/4 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF4B | Ethernet1/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF4B | Ethernet1/2 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF4B | Ethernet1/3 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF4B | Ethernet1/4 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF5A | Ethernet1/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF5A | Ethernet1/2 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF5A | Ethernet1/3 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF5A | Ethernet1/4 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF5B | Ethernet1/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF5B | Ethernet1/2 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF5B | Ethernet1/3 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF5B | Ethernet1/4 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF6A | Ethernet1/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF6A | Ethernet1/2 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF6A | Ethernet1/3 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF6A | Ethernet1/4 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF6B | Ethernet1/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF6B | Ethernet1/2 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF6B | Ethernet1/3 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF6B | Ethernet1/4 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF7A | Ethernet1/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF7A | Ethernet1/2 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF7A | Ethernet1/3 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF7A | Ethernet1/4 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF7B | Ethernet1/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF7B | Ethernet1/2 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF7B | Ethernet1/3 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF7B | Ethernet1/4 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF8A | Ethernet1/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF8A | Ethernet1/2 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF8A | Ethernet1/3 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF8A | Ethernet1/4 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF8B | Ethernet1/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF8B | Ethernet1/2 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF8B | Ethernet1/3 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF8B | Ethernet1/4 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF9A | Ethernet1/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF9A | Ethernet1/2 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF9A | Ethernet1/3 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF9A | Ethernet1/4 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF9B | Ethernet1/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF9B | Ethernet1/2 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF9B | Ethernet1/3 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF9B | Ethernet1/4 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF10A | Ethernet1/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF10A | Ethernet1/2 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF10A | Ethernet1/3 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF10A | Ethernet1/4 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF10B | Ethernet1/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF10B | Ethernet1/2 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF10B | Ethernet1/3 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF10B | Ethernet1/4 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF11A | Ethernet1/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF11A | Ethernet1/2 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF11A | Ethernet1/3 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF11A | Ethernet1/4 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF11B | Ethernet1/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF11B | Ethernet1/2 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF11B | Ethernet1/3 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF11B | Ethernet1/4 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF12A | Ethernet1/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF12A | Ethernet1/2 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF12A | Ethernet1/3 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF12A | Ethernet1/4 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF12B | Ethernet1/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF12B | Ethernet1/2 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF12B | Ethernet1/3 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF12B | Ethernet1/4 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF13A | Ethernet1/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF13A | Ethernet1/2 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF13A | Ethernet1/3 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF13A | Ethernet1/4 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF13B | Ethernet1/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF13B | Ethernet1/2 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF13B | Ethernet1/3 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF13B | Ethernet1/4 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF14A | Ethernet1/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF14A | Ethernet1/2 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF14A | Ethernet1/3 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF14A | Ethernet1/4 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF14B | Ethernet1/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF14B | Ethernet1/2 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF14B | Ethernet1/3 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF14B | Ethernet1/4 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-SPINE1 | Ethernet1 | 172.16.2.1/31 | DC1-SUPER-SPINE1 | Ethernet1 | 172.16.32.6/31 |
| DC1-POD2-SPINE1 | Ethernet2 | 172.16.2.65/31 | DC1-SUPER-SPINE2 | Ethernet2 | 172.16.32.70/31 |
| DC1-POD2-SPINE1 | Ethernet3 | 172.16.2.129/31 | DC1-SUPER-SPINE3 | Ethernet3 | 172.16.32.134/31 |
| DC1-POD2-SPINE2 | Ethernet1 | 172.16.2.3/31 | DC1-SUPER-SPINE1 | Ethernet1 | 172.16.32.6/31 |
| DC1-POD2-SPINE2 | Ethernet2 | 172.16.2.67/31 | DC1-SUPER-SPINE2 | Ethernet2 | 172.16.32.70/31 |
| DC1-POD2-SPINE2 | Ethernet3 | 172.16.2.131/31 | DC1-SUPER-SPINE3 | Ethernet3 | 172.16.32.134/31 |
| DC1-POD2-SPINE3 | Ethernet1 | 172.16.2.5/31 | DC1-SUPER-SPINE1 | Ethernet17/1 | 172.16.2.6/31 |
| DC1-POD2-SPINE3 | Ethernet2 | 172.16.2.69/31 | DC1-SUPER-SPINE2 | Ethernet17/2 | 172.16.2.70/31 |
| DC1-POD2-SPINE3 | Ethernet3 | 172.16.2.133/31 | DC1-SUPER-SPINE3 | Ethernet17/3 | 172.16.2.134/31 |
| DC1-POD2-SPINE3 | Ethernet4 | 172.16.2.197/31 | DC1-SUPER-SPINE4 | Ethernet17/4 | 172.16.2.198/31 |
| DC1-POD2-SPINE4 | Ethernet1 | 172.16.2.7/31 | DC1-SUPER-SPINE1 | Ethernet17/1 | 172.16.2.6/31 |
| DC1-POD2-SPINE4 | Ethernet2 | 172.16.2.71/31 | DC1-SUPER-SPINE2 | Ethernet17/2 | 172.16.2.70/31 |
| DC1-POD2-SPINE4 | Ethernet3 | 172.16.2.135/31 | DC1-SUPER-SPINE3 | Ethernet17/3 | 172.16.2.134/31 |
| DC1-POD2-SPINE4 | Ethernet4 | 172.16.2.199/31 | DC1-SUPER-SPINE4 | Ethernet17/4 | 172.16.2.198/31 |
| DC1-SUPER-SPINE1 | Ethernet1 | 172.16.32.6/31 | DC2-POD1-SPINE4 | Ethernet1 | 172.16.32.7/31 |
| DC1-SUPER-SPINE2 | Ethernet2 | 172.16.32.70/31 | DC2-POD1-SPINE4 | Ethernet2 | 172.16.32.71/31 |
| DC1-SUPER-SPINE3 | Ethernet3 | 172.16.32.134/31 | DC2-POD1-SPINE4 | Ethernet3 | 172.16.32.135/31 |
| DC1-SUPER-SPINE4 | Ethernet4 | 172.16.32.198/31 | DC2-POD1-SPINE4 | Ethernet4 | 172.16.32.199/31 |
| DC2-POD1-LEAF1A | Ethernet5 | 11.1.1.18/31 | DC2-POD1-LEAF1B | Ethernet5 | 11.1.1.19/31 |

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.4.1.0/24 | 256 | 28 | 10.94 % |
| 10.4.2.0/24 | 256 | 28 | 10.94 % |
| 10.4.27.0/24 | 256 | 5 | 1.96 % |
| 10.4.28.0/24 | 256 | 4 | 1.57 % |
| 10.4.29.0/24 | 256 | 4 | 1.57 % |
| 10.4.32.0/24 | 256 | 28 | 10.94 % |
| 10.4.58.0/24 | 256 | 4 | 1.57 % |
| 172.16.200.0/24 | 256 | 2 | 0.79 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC1_POD1 | DC1-POD1-LEAF1A | 10.4.1.3/32 |
| DC1_POD1 | DC1-POD1-LEAF1B | 10.4.1.4/32 |
| DC1_POD1 | DC1-POD1-LEAF2A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF2B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF3A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF3B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF4A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF4B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF5A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF5B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF6A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF6B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF7A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF7B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF8A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF8B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF9A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF9B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF10A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF10B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF11A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF11B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF12A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF12B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF13A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF13B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF14A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF14B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-SPINE1 | 10.4.28.1/32 |
| DC1_POD1 | DC1-POD1-SPINE2 | 10.4.28.2/32 |
| DC1_POD1 | DC1-POD1-SPINE3 | 10.4.28.3/32 |
| DC1_POD1 | DC1-POD1-SPINE4 | 10.4.28.4/32 |
| DC1_POD2 | DC1-POD2-LEAF1A | 10.4.2.3/32 |
| DC1_POD2 | DC1-POD2-LEAF1B | 10.4.2.4/32 |
| DC1_POD2 | DC1-POD2-LEAF2A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF2B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF3A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF3B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF4A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF4B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF5A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF5B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF6A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF6B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF7A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF7B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF8A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF8B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF9A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF9B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF10A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF10B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF11A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF11B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF12A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF12B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF13A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF13B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF14A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF14B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-SPINE1 | 10.4.29.1/32 |
| DC1_POD2 | DC1-POD2-SPINE2 | 10.4.29.2/32 |
| DC1_POD2 | DC1-POD2-SPINE3 | 10.4.29.3/32 |
| DC1_POD2 | DC1-POD2-SPINE4 | 10.4.29.4/32 |
| DC1 | DC1-SUPER-SPINE1 | 10.4.27.1/32 |
| DC1 | DC1-SUPER-SPINE2 | 10.4.27.2/32 |
| DC1 | DC1-SUPER-SPINE3 | 10.4.27.3/32 |
| DC1 | DC1-SUPER-SPINE4 | 10.4.27.4/32 |
| DC1 | DC1-SUPER-SPINE5 | 10.4.27.5/32 |
| DC2_POD1 | DC2-POD1-LEAF1A | 10.4.32.3/32 |
| DC2_POD1 | DC2-POD1-LEAF1B | 10.4.32.4/32 |
| DC2_POD1 | DC2-POD1-LEAF2A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF2B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF3A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF3B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF4A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF4B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF5A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF5B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF6A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF6B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF7A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF7B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF8A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF8B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF9A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF9B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF10A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF10B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF11A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF11B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF12A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF12B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF13A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF13B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF14A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF14B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-SPINE1 | 10.4.58.1/32 |
| DC2_POD1 | DC2-POD1-SPINE2 | 10.4.58.2/32 |
| DC2_POD1 | DC2-POD1-SPINE3 | 10.4.58.3/32 |
| DC2_POD1 | DC2-POD1-SPINE4 | 10.4.58.4/32 |
| DC2 | DC2-SUPER-SPINE1 | 172.16.200.1/32 |
| DC2 | DC2-SUPER-SPINE2 | 172.16.200.2/32 |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 10.5.1.0/24 | 256 | 28 | 10.94 % |
| 10.5.2.0/24 | 256 | 28 | 10.94 % |
| 10.5.32.0/24 | 256 | 28 | 10.94 % |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DC1_POD1 | DC1-POD1-LEAF1A | 10.5.1.3/32 |
| DC1_POD1 | DC1-POD1-LEAF1B | 10.5.1.3/32 |
| DC1_POD1 | DC1-POD1-LEAF2A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF2B | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF3A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF3B | 10.5.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF4A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF4B | 10.5.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF5A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF5B | 10.5.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF6A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF6B | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF7A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF7B | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF8A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF8B | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF9A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF9B | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF10A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF10B | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF11A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF11B | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF12A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF12B | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF13A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF13B | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF14A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF14B | 10.5.1.5/32 |
| DC1_POD2 | DC1-POD2-LEAF1A | 10.5.2.3/32 |
| DC1_POD2 | DC1-POD2-LEAF1B | 10.5.2.3/32 |
| DC1_POD2 | DC1-POD2-LEAF2A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF2B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF3A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF3B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF4A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF4B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF5A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF5B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF6A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF6B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF7A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF7B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF8A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF8B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF9A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF9B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF10A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF10B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF11A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF11B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF12A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF12B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF13A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF13B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF14A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF14B | 10.5.2.5/32 |
| DC2_POD1 | DC2-POD1-LEAF1A | 10.5.32.3/32 |
| DC2_POD1 | DC2-POD1-LEAF1B | 10.5.32.3/32 |
| DC2_POD1 | DC2-POD1-LEAF2A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF2B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF3A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF3B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF4A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF4B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF5A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF5B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF6A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF6B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF7A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF7B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF8A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF8B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF9A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF9B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF10A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF10B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF11A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF11B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF12A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF12B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF13A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF13B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF14A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF14B | 10.5.32.5/32 |

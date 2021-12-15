# DC1-POD1-LEAF3B
# Table of Contents
<!-- toc -->

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Domain-list](#domain-list)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [ACL](#acl)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Quality Of Service](#quality-of-service)
- [EOS CLI](#eos-cli)

<!-- toc -->
# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | oob_management | oob | mgmt | 192.168.1.11/16 | 10.6.1.1 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management0 | oob_management | oob | mgmt | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management0
   description oob_management
   no shutdown
   vrf mgmt
   ip address 192.168.1.11/16
```

## Domain-list

### Domain-list:
 - structured-config.set.under.vrf.common-vrf

### Domain-list Device Configuration

```eos
!
ip domain-list structured-config.set.under.vrf.common-vrf
!
```

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS |
| ---------- | ---------- |
| default | true |

### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| mgmt | - | - |


### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf mgmt
      no shutdown
```

# Authentication

## Local Users

### Local Users Summary

| User | Privilege | Role |
| ---- | --------- | ---- |
| admin | 15 | network-admin |

### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 $6$82gqIqw8b3nibNrk$MoZO0S8QMQN8uwnR8v48dbGrL0Ec/6q36tSx8y9IsExi4L.HtmokW9rX8VehLxhg542mNTBKqxMBF.LgnCTm4.
```

# Monitoring

## SNMP

### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | AMS DC1 DC1_POD1 DC1-POD1-LEAF3B | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location AMS DC1 DC1_POD1 DC1-POD1-LEAF3B
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **rstp**

### Global Spanning-Tree Settings

Global RSTP priority: 4096

## Spanning Tree Device Configuration

```eos
!
spanning-tree mode rstp
spanning-tree priority 4096
```

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

## Internal VLAN Allocation Policy Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet29/1 | P2P_LINK_TO_DC1-POD1-SPINE1_Ethernet6/1 | routed | - | 172.17.1.25/31 | default | 9214 | false | - | - |
| Ethernet30/1 | P2P_LINK_TO_DC1-POD1-SPINE2_Ethernet6/1 | routed | - | 172.17.1.27/31 | default | 9214 | false | - | - |
| Ethernet31/1 | P2P_LINK_TO_DC1-POD1-SPINE3_Ethernet6/1 | routed | - | 172.17.1.29/31 | default | 9214 | false | - | - |
| Ethernet32/1 | P2P_LINK_TO_DC1-POD1-SPINE4_Ethernet6/1 | routed | - | 172.17.1.31/31 | default | 9214 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet29/1
   description P2P_LINK_TO_DC1-POD1-SPINE1_Ethernet6/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.25/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet30/1
   description P2P_LINK_TO_DC1-POD1-SPINE2_Ethernet6/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.27/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet31/1
   description P2P_LINK_TO_DC1-POD1-SPINE3_Ethernet6/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.29/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet32/1
   description P2P_LINK_TO_DC1-POD1-SPINE4_Ethernet6/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.31/31
   ptp enable
   service-profile QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.4.1.6/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 10.5.1.6/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 10.4.1.6/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 10.5.1.6/32
```

## VXLAN Interface

### VXLAN Interface Summary

#### Source Interface: Loopback1

#### UDP port: 4789

#### VRF to VNI Mappings

| VLAN | VNI |
| ---- | --- |
| Common_VRF | 1025 |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description DC1-POD1-LEAF3B_VTEP
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vrf Common_VRF vni 1025
```

# Routing
## Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

## Virtual Router MAC Address

### Virtual Router MAC Address Summary

#### Virtual Router MAC Address: 00:1c:73:00:dc:01

### Virtual Router MAC Address Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:dc:01
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true|| Common_VRF | true |
| mgmt | false |

### IP Routing Device Configuration

```eos
!
ip routing
ip routing vrf Common_VRF
no ip routing vrf mgmt
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false || Common_VRF | false |
| mgmt | false |


## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| mgmt  | 0.0.0.0/0 |  10.6.1.1  |  -  |  1  |  -  |  -  |  - |

### Static Routes Device Configuration

```eos
!
ip route vrf mgmt 0.0.0.0/0 10.6.1.1
```

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65111.300|  10.4.1.6 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 4 ecmp 4 |

### Router BGP Peer Groups

#### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Next-hop unchanged | True |
| Source | Loopback0 |
| Bfd | true |
| Ebgp multihop | 5 |
| Send community | all |
| Maximum routes | 0 (no limit) |

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Send-community | Maximum-routes |
| -------- | --------- | --- | -------------- | -------------- |
| 172.17.1.24 | 65001.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.26 | 65001.102 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.28 | 65001.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.30 | 65001.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |

### Router BGP EVPN Address Family

- VPN import pruning is __enabled__

#### Router BGP EVPN MAC-VRFs

#### Router BGP EVPN VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Common_VRF | 10.4.1.6:1025 | connected |

### Router BGP Device Configuration

```eos
!
router bgp 65111.300
   router-id 10.4.1.6
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS next-hop-unchanged
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 5
   neighbor EVPN-OVERLAY-PEERS password 7 q+VNViP5i4rVjW1cxFv2wA==
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.17.1.24 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.24 remote-as 65001.100
   neighbor 172.17.1.24 description DC1-POD1-SPINE1_Ethernet6/1
   neighbor 172.17.1.26 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.26 remote-as 65001.102
   neighbor 172.17.1.26 description DC1-POD1-SPINE2_Ethernet6/1
   neighbor 172.17.1.28 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.28 remote-as 65001.100
   neighbor 172.17.1.28 description DC1-POD1-SPINE3_Ethernet6/1
   neighbor 172.17.1.30 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.30 remote-as 65001.100
   neighbor 172.17.1.30 description DC1-POD1-SPINE4_Ethernet6/1
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
      route import match-failure action discard
   !
   address-family rt-membership
      neighbor EVPN-OVERLAY-PEERS activate
      neighbor EVPN-OVERLAY-PEERS default-route-target only
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
   !
   vrf Common_VRF
      rd 10.4.1.6:1025
      route-target import evpn 1025:1025
      route-target export evpn 1025:1025
      router-id 10.4.1.6
      redistribute connected
      !
      comment
      Comment created from raw_eos_cli under BGP for VRF Common_VRF
      EOF

```

# BFD

## Router BFD

### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 300 min-rx 300 multiplier 3
```

# Multicast

## IP IGMP Snooping

### IP IGMP Snooping Summary

IGMP snooping is globally enabled.


### IP IGMP Snooping Device Configuration

```eos
```

# Filters

## Prefix-lists

### Prefix-lists Summary

#### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.4.1.0/24 eq 32 |
| 20 | permit 10.5.1.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.4.1.0/24 eq 32
   seq 20 permit 10.5.1.0/24 eq 32
```

## Route-maps

### Route-maps Summary

#### RM-CONN-2-BGP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |

### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
```

# ACL

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| Common_VRF | enabled |
| mgmt | disabled |

## VRF Instances Device Configuration

```eos
!
vrf instance Common_VRF
!
vrf instance mgmt
```

# Quality Of Service

# EOS CLI

```eos
!
interface Loopback1111
  description Loopback created from raw_eos_cli under platform_settings vEOS-LAB

interface Loopback1000
  description Loopback created from raw_eos_cli under VRF Common_VRF

```
